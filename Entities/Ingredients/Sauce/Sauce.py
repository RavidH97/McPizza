from abc import ABC
from Entities.Ingredients.Ingredient import Ingredient


class Sauce(Ingredient, ABC):
    """Sauce class"""
    _class_name = "Sauce"

    def __init__(self):
        """Initialize Sauce."""
        super().__init__()


# Example usage
if __name__ == "__main__":
    class TomatoSauce(Sauce):
        """Tomato Sauce class"""

        _class_name = "Tomato Sauce"

        @classmethod
        def get_name(cls) -> str:
            return cls._class_name

        @classmethod
        def is_vegan(cls) -> bool:
            return True

        @classmethod
        def is_dairy(cls) -> bool:
            return False


    obj = TomatoSauce()
    print(f"Am I dairy? {obj.is_dairy()}")
