from typing import Optional
from plyer import notification

import datetime
import inspect

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

    valid_modes = ["simple", "detailed", "file"]

    def __init__(self, mode: str= "simple", show_file: bool = False, show_tag: bool = False, enable_all: bool = False, notice: bool = False, tag: Optional[str]= None):
        """
        mode:
            - "simple" : [+] msg
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
        """
        if enable_all:
            show_file = True
            show_tag  = True
            notice    = True

        self.mode = mode.lower()
        self.show_tag = show_tag
        self.show_file = show_file
        self.notice = notice
        self.tag = tag
        
        if self.mode not in self.valid_modes:
            raise ValueError(f"Invalid mode '{mode}' specified. Valid modes are: {', '.join(self.valid_modes)}")
        

    def GetTime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def GetCaller(self) -> str:
        frame = inspect.stack()[3]
        filename = frame.filename.split("/")[-1]
        lineno = frame.lineno
        return f"{filename}:{lineno}"
    
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
            symbol = self.SYMBOLS.get(type, "[?]")
            if self.show_file:
                formatted = f"[{caller}][{tag_str}]{colors}{symbol}{self.RESET} {msg}"
            else:
                formatted = f"{colors}{symbol}{self.RESET} {msg}"

        elif self.mode == "file":
            formatted = f"[{caller}]{colors}[{types}]{self.RESET} {msg}"

        else:
            time = self.GetTime()
            formatted = f"[{time}]{colors}[{types}]{self.RESET}"
            if final_tag:
                formatted += f"[{final_tag}]"
            if self.show_file:
                formatted += f"[{caller}]"
            formatted += f" : {msg}"

        print(formatted)

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