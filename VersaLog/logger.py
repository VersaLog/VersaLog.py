import datetime

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

    def __init__(self, mode: str = "simple"):
        """
        mode:
            - "simple" : [+] msg
            - "detailed" : [TIME][LEVEL] : msg
        """
        self.mode = mode.lower()

    def GetTime(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def Log(self, msg: str, type: str) -> None:
        colors = self.COLORS.get(type, "")
        types = type.upper()

        if self.mode == "simple":
            symbol = self.SYMBOLS.get(type, "[?]")
            formatted = f"{colors}{symbol}{self.RESET} {msg}"
        else:
            time = self.GetTime()
            formatted = f"[{time}]{colors}[{types}]{self.RESET} : {msg}"

        print(formatted)

    def info(self, msg: str) -> None:
        self.Log(msg, "INFO")

    def err(self, msg: str) -> None:
        self.Log(msg, "ERROR")

    def war(self, msg: str) -> None:
        self.Log(msg, "WARNING")