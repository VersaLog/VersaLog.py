import datetime
import inspect

class VersaLog:
    COLORS = {
        "INFO": "\033[32m",
        "ERROR": "\033[31m",
        "WARNING": "\033[33m",
    }

    SYMBOLS = {
        "INFO": "[+]",
        "ERROR": "[-]",
        "WARNING": "[!]",
    }
    
    RESET = "\033[0m"

    def __init__(self, mode: str = "simple", show_file: bool = False):
        """
        mode:
            - "simple" : [+] msg
            - "detailed" : [TIME][LEVEL] : msg
            - "file" : [FILE:LINE][LEVEL] msg
        show_file:
            - True : Display filename and line number (for simple and detailed modes)
        """
        self.mode = mode.lower()
        self.show_file = show_file

    def GetTime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def GetCaller(self) -> str:
        frame = inspect.stack()[3]
        filename = frame.filename.split("/")[-1]
        lineno = frame.lineno
        return f"{filename}:{lineno}"
    
    def Log(self, msg: str, type: str) -> None:
        colors = self.COLORS.get(type, "")
        types = type.upper()

        caller = self.GetCaller() if self.show_file or self.mode == "file" else ""

        if self.mode == "simple":
            symbol = self.SYMBOLS.get(type, "[?]")
            if self.show_file:
                formatted = f"[{caller}]{colors}{symbol}{self.RESET} {msg}"
            else:
                formatted = f"{colors}{symbol}{self.RESET} {msg}"

        elif self.mode == "file":
            formatted = f"[{caller}]{colors}[{types}]{self.RESET} {msg}"

        else:
            time = self.GetTime()
            if self.show_file:
                formatted = f"[{time}]{colors}[{types}]{self.RESET}[{caller}] : {msg}"
            else:
                formatted = f"[{time}]{colors}[{types}]{self.RESET} : {msg}"

        print(formatted)

    def info(self, msg: str) -> None:
        self.Log(msg, "INFO")

    def err(self, msg: str) -> None:
        self.Log(msg, "ERROR")

    def war(self, msg: str) -> None:
        self.Log(msg, "WARNING")