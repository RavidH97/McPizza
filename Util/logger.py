from datetime import datetime
from threading import Lock


class Logger:
    """Basic logger to print useful information"""
    _lock = Lock()

    def __init__(self, name: str):
        """Initialize Logger with a name."""
        self.name = name

    def log(self, message: str):
        """Prints a message."""
        with self._lock:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {self.name} - {message}")


# Example usage
if __name__ == "__main__":
    obj = Logger("Ravid")
    obj.log("Hi! How are you?")
