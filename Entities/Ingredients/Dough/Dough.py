from abc import ABC, abstractmethod
from Entities.Ingredients.Ingredient import Ingredient


class Dough(Ingredient, ABC):
    """Dough class"""
    _class_name = "Dough"

    def __init__(self):
        """Initialize Dough."""
        super().__init__()

    @classmethod
    @abstractmethod
    def flour_type(cls) -> str:
        pass


# Example usage
if __name__ == "__main__":
    class CornDough(Dough):
        """Corn Dough class"""

        _class_name = "Corn Dough"

        @classmethod
        def get_name(cls) -> str:
            return cls._class_name

        @classmethod
        def is_vegan(cls) -> bool:
            return True

        @classmethod
        def is_dairy(cls) -> bool:
            return False

        @classmethod
        def flour_type(cls) -> str:
            return "Corn"

    obj = CornDough()
    print(f"I use {obj.flour_type()} flour")
