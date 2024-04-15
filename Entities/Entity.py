from abc import abstractmethod, ABC

from Util.logger import Logger


class Entity(ABC):
    """Base entity model."""

    def __init__(self):
        """Initialize Entity."""
        self.logger = Logger(self.entity_name)

    @classmethod
    @abstractmethod
    def class_name(cls) -> str:
        pass

    @property
    @abstractmethod
    def entity_name(self) -> str:
        pass

    def _log(self, message: str):
        """Log a message from the entity."""
        self.logger.log(message)


# Example usage
if __name__ == "__main__":

    class Fish(Entity):
        """Fish class"""

        _class_name = "Fish"

        @classmethod
        @property
        def class_name(cls) -> str:
            return cls._class_name

        def __init__(self, fish_name: str):
            """Initialize Fish."""
            self._fish_name = fish_name
            self._entity_name = self.class_name + " " + self._fish_name
            super().__init__()

        @property
        def entity_name(self) -> str:
            """Gets entity name."""
            return self._entity_name

        def find_dori(self):
            self._log("Did you see Dori??")


    obj = Fish("Nemo")
    obj.find_dori()
