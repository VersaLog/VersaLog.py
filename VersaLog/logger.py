from typing import Optional
from plyer import notification

import datetime
import inspect
import os

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

    def __init__(self, mode: str= "simple", tag: Optional[str]= None, show_file: bool = False, show_tag: bool = False, enable_all: bool = False, notice: bool = False, all_save: bool = False, save_levels: Optional[list]=None):
        """
        mode:
            - "simple" : [+] msg
            - "simple2" : [TIME] [+] msg
            - "detailed" : [TIME][LEVEL] : msg
            - "file" : [FILE:LINE][LEVEL] msg
        show_file:
            - True : Display filename and line number (for simple and detailed modes)
        show_tag:
            - True : Show self.tag if no explicit tag is provided
        tag:
            - Default tag to use when show_tag is enabled
        enable_all:
            - Shortcut to enable both show_file and show_tag and notice
        notice:
            - True : When an error or critical level log is output, a desktop notification (using plyer.notification) will be displayed. The notification includes the log level and message.
        all_save:
            - True : When an error or critical level log is output, the log will be saved to a file.
        save_levels:
            - A list of log levels to save. Defaults to ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"].
        """
        if enable_all:
            show_file = True
            show_tag  = True
            notice    = True
            all_save  = True

        self.mode = mode.lower()
        self.show_tag = show_tag
        self.show_file = show_file
        self.notice = notice
        self.tag = tag
        self.all_save = all_save
        self.save_levels = save_levels
        
        if self.mode not in self.valid_modes:
            raise ValueError(f"Invalid mode '{mode}' specified. Valid modes are: {', '.join(self.valid_modes)}")
        
        if self.all_save:
            if self.save_levels is None:
                self.save_levels = self.valid_save_levels.copy()
            elif not isinstance(self.save_levels, list):
                raise ValueError(f"save_levels must be a list. Example: ['ERROR']")
            elif not all(level in self.valid_save_levels for level in self.save_levels):
                raise ValueError(f"Invalid save_levels specified. Valid levels are: {', '.join(self.valid_save_levels)}")


    def GetTime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def GetCaller(self) -> str:
        frame = inspect.stack()[3]
        filename = frame.filename.split("/")[-1]
        lineno = frame.lineno
        return f"{filename}:{lineno}"
    
    def save_log(self, log_text: str, level: str) -> None:
        if level not in self.save_levels:
            return
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_text + '\n')

    def Log(self, msg: str, tye: str, tag: Optional[str] = None) -> None:
        colors = self.COLORS.get(tye, "")
        types = tye.upper()

        final_tag = tag or (self.tag if self.show_tag else None)
        tag_str = final_tag if final_tag else ""

        caller = self.GetCaller() if self.show_file or self.mode == "file" else ""

        if self.notice and types in ["ERROR", "CRITICAL"]:
            notification.notify(
                title=f"{types} Log notice",
                message=msg,
                app_name="VersaLog"
            )

        if self.mode == "simple":
            symbol = self.SYMBOLS.get(tye, "[?]")
            if self.show_file:
                formatted = f"[{caller}][{tag_str}]{colors}{symbol}{self.RESET} {msg}"
                plain = f"[{caller}][{tag_str}]{symbol} {msg}"
            else:
                formatted = f"{colors}{symbol}{self.RESET} {msg}"
                plain = f"{symbol} {msg}"

        elif self.mode == "simple2":
            symbol = self.SYMBOLS.get(tye, "[?]")
            time = self.GetTime()
            if self.show_file:
                formatted = f"[{time}] [{caller}][{tag_str}]{colors}{symbol}{self.RESET} {msg}"
                plain = f"[{time}] [{caller}][{tag_str}]{symbol} {msg}"
            else:
                formatted = f"[{time}] {colors}{symbol}{self.RESET} {msg}"
                plain = f"[{time}] {symbol} {msg}"

        elif self.mode == "file":
            formatted = f"[{caller}]{colors}[{types}]{self.RESET} {msg}"
            plain = f"[{caller}][{types}] {msg}"

        else:
            time = self.GetTime()
            formatted = f"[{time}]{colors}[{types}]{self.RESET}"
            plain = f"[{time}][{types}]"
            if final_tag:
                formatted += f"[{final_tag}]"
                plain += f"[{final_tag}]"
            if self.show_file:
                formatted += f"[{caller}]"
                plain += f"[{caller}]"
            formatted += f" : {msg}"
            plain += f" : {msg}"

        print(formatted)
        self.save_log(plain, types)

    def info(self, msg: str, tag: Optional[str] = None) -> None:
        self.Log(msg, "INFO", tag)

    def error(self, msg: str, tag: Optional[str] = None) -> None:
        self.Log(msg, "ERROR", tag)

    def warning(self, msg: str, tag: Optional[str] = None) -> None:
        self.Log(msg, "WARNING", tag)

    def debug(self, msg: str, tag: Optional[str] = None) -> None:
        self.Log(msg, "DEBUG", tag)

    def critical(self, msg: str, tag: Optional[str] = None) -> None:
        self.Log(msg, "CRITICAL", tag)