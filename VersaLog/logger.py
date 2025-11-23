from typing import Optional, Union, List
from plyer import notification

import datetime
import inspect
import os
import sys
import time
import queue
import threading
import traceback

class VersaLog:
    COLORS = {
        "INFO": "\033[32m",
        "ERROR": "\033[31m",
        "WARNING": "\033[33m",
        "DEBUG": "\033[36m",
        "CRITICAL": "\033[35m",
    }

    SYMBOLS = {
        "INFO": "[+]",
        "ERROR": "[-]",
        "WARNING": "[!]",
        "DEBUG": "[D]",
        "CRITICAL": "[C]",
    }
    
    RESET = "\033[0m"

    valid_modes = ["simple", "simple2", "detailed", "file"]
    valid_save_levels = ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"]

    def __init__(self, enum: str= "simple", tag: Optional[Union[str, List[str]]]= None, show_file: bool = False, show_tag: bool = False, enable_all: bool = False, notice: bool = False, all_save: bool = False, save_levels: Optional[list]=None, silent: bool = False, catch_exceptions: bool = False):
        """
        enum:
            - "simple" : [+] msg
            - "simple2" : [TIME] [+] msg
            - "detailed" : [TIME][LEVEL] : msg
            - "file" : [FILE:LINE][LEVEL] msg
        show_file:
            - True : Display filename and line number (for simple and detailed enum)
        show_tag:
            - True : Show self.tag if no explicit tag is provided
        tag:
            - Default tag to use when show_tag is enabled (str or list[str])
        enable_all:
            - Shortcut to enable both show_file and show_tag and notice
        notice:
            - True : When an error or critical level log is output, a desktop notification (using plyer.notification) will be displayed. The notification includes the log level and message.
        all_save:
            - True : When an error or critical level log is output, the log will be saved to a file.
        save_levels:
            - A list of log levels to save. Defaults to ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"]
        silent:
            - True : Suppress standard output (print)
        catch_exceptions:
            - True : Automatically catch unhandled exceptions and log them as critical
        """
        if enable_all:
            show_file = True
            show_tag  = True
            notice    = True
            all_save  = True

        self.enum = enum.lower()
        self.show_tag = show_tag
        self.show_file = show_file
        self.notice = notice
        self.tag = tag if (tag is None or isinstance(tag, list)) else [tag] if isinstance(tag, str) and ',' in tag else tag
        self.all_save = all_save
        self.save_levels = save_levels
        self.silent = silent

        self.log_queue = queue.Queue()
        self.worker_thread = threading.Thread(target=self._worker, daemon=True)
        self.worker_thread.start()

        self._last_cleanup_date = None
        
        if self.enum not in self.valid_modes:
            raise ValueError(f"Invalid enum '{enum}' specified. Valid modes are: {', '.join(self.valid_modes)}")
        
        if self.all_save:
            if self.save_levels is None:
                self.save_levels = self.valid_save_levels.copy()
            elif not isinstance(self.save_levels, list):
                raise ValueError(f"save_levels must be a list. Example: ['ERROR']")
            elif not all(level in self.valid_save_levels for level in self.save_levels):
                raise ValueError(f"Invalid save_levels specified. Valid levels are: {', '.join(self.valid_save_levels)}")
            
        if catch_exceptions:
            sys.excepthook = self._handle_exception

    def _handle_exception(self, exc_type, exc_value, exc_traceback):
        tb_str = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.critical(f"Unhandled exception:\n{tb_str}")

    def _worker(self):
        while True:
            log_text, level = self.log_queue.get()
            if log_text is None:
                break
            self._save_log_sync(log_text, level)
            self.log_queue.task_done()

    def _GetTime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _GetCaller(self) -> str:
        frame = inspect.stack()[3]
        filename = frame.filename.split("/")[-1]
        lineno = frame.lineno
        return f"{filename}:{lineno}"

    def _cleanup_old_logs(self, days: int = 7) -> None:
        log_dir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(log_dir):
            return

        now = datetime.datetime.now()
        for filename in os.listdir(log_dir):
            if not filename.endswith(".log"):
                continue
            filepath = os.path.join(log_dir, filename)

            try:
                file_date = datetime.datetime.strptime(filename.replace(".log", ""), "%Y-%m-%d")
            except ValueError:
                file_date = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

            if (now - file_date).days >= days:
                try:
                    os.remove(filepath)
                    if not self.silent:
                        self.info(f"[LOG CLEANUP] removed: {filepath}")
                except Exception as e:
                    if not self.silent:
                        self.warning(f"[LOG CLEANUP WARNING] {filepath} cannot be removed: {e}")
    
    def _save_log_sync(self, log_text: str, level: str) -> None:
        if not self.all_save:
            return
        if level not in self.save_levels:
            return
        log_dir = os.path.join(os.getcwd(), 'log')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_text + '\n')

        today = datetime.date.today()
        if self._last_cleanup_date != today:
            self._cleanup_old_logs(days=7)
            self._last_cleanup_date = today
    
    def _save_log(self, log_text: str, level: str) -> None:
        if not self.all_save:
            return
        if level not in self.save_levels:
            return
        log_dir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_text + '\n')

    def _Log(self, msg: str, tye: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        colors = self.COLORS.get(tye, "")
        types = tye.upper()

        final_tag = tag if tag is not None else (self.tag if self.show_tag else None)
        if isinstance(final_tag, list):
            tags = [str(t) for t in final_tag if t]
        elif isinstance(final_tag, str):
            tags = [final_tag] if final_tag else []
        else:
            tags = []
        tag_str = "".join(f"[{t}]" for t in tags) if tags else ""

        caller = self._GetCaller() if self.show_file or self.enum == "file" else ""

        if self.enum == "simple":
            symbol = self.SYMBOLS.get(tye, "[?]")
            if self.show_file:
                formatted = f"[{caller}]{tag_str}{colors}{symbol}{self.RESET} {msg}" if tag_str else f"[{caller}]{colors}{symbol}{self.RESET} {msg}"
                plain = f"[{caller}]{tag_str}{symbol} {msg}" if tag_str else f"[{caller}]{symbol} {msg}"
            else:
                formatted = f"{tag_str}{colors}{symbol}{self.RESET} {msg}" if tag_str else f"{colors}{symbol}{self.RESET} {msg}"
                plain = f"{tag_str}{symbol} {msg}" if tag_str else f"{symbol} {msg}"

        elif self.enum == "simple2":
            symbol = self.SYMBOLS.get(tye, "[?]")
            time = self._GetTime()
            if self.show_file:
                formatted = f"[{time}] [{caller}]{tag_str}{colors}{symbol}{self.RESET} {msg}" if tag_str else f"[{time}] [{caller}]{colors}{symbol}{self.RESET} {msg}"
                plain = f"[{time}] [{caller}]{tag_str}{symbol} {msg}" if tag_str else f"[{time}] [{caller}]{symbol} {msg}"
            else:
                formatted = f"[{time}] {tag_str}{colors}{symbol}{self.RESET} {msg}" if tag_str else f"[{time}] {colors}{symbol}{self.RESET} {msg}"
                plain = f"[{time}] {tag_str}{symbol} {msg}" if tag_str else f"[{time}] {symbol} {msg}"

        elif self.enum == "file":
            formatted = f"[{caller}]{tag_str}{colors}[{types}]{self.RESET} {msg}" if tag_str else f"[{caller}]{colors}[{types}]{self.RESET} {msg}"
            plain = f"[{caller}]{tag_str}[{types}] {msg}" if tag_str else f"[{caller}][{types}] {msg}"

        else:  # detailed
            time = self._GetTime()
            formatted = f"[{time}]{colors}[{types}]{self.RESET}{tag_str}" if tag_str else f"[{time}]{colors}[{types}]{self.RESET}"
            plain = f"[{time}][{types}]{tag_str}" if tag_str else f"[{time}][{types}]"
            if self.show_file:
                formatted += f"[{caller}]"
                plain += f"[{caller}]"
            formatted += f" : {msg}"
            plain += f" : {msg}"

        if not self.silent:
            print(formatted)

        self._save_log(plain, types)

    def info(self, msg: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        self._Log(msg, "INFO", tag)

    def error(self, msg: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        self._Log(msg, "ERROR", tag)

    def warning(self, msg: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        self._Log(msg, "WARNING", tag)

    def debug(self, msg: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        self._Log(msg, "DEBUG", tag)

    def critical(self, msg: str, tag: Optional[Union[str, List[str]]] = None) -> None:
        self._Log(msg, "CRITICAL", tag)

    def board(self):
        print("=" * 45)