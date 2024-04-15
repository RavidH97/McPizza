from abc import ABC
from Entities.Ingredients.Ingredient import Ingredient


class Cheese(Ingredient, ABC):
    """Cheese class"""
    _class_name = "Cheese"

    def __init__(self):
        """Initialize Cheese."""
        super().__init__()


# Example usage
if __name__ == "__main__":
    class MozzarellaCheese(Cheese):
        """Mozzarella Cheese class"""

        _class_name = "Mozzarella Cheese"

        @classmethod
        def get_name(cls) -> str:
            return cls._class_name

        @classmethod
        def is_vegan(cls) -> bool:
            return False

        @classmethod
        def is_dairy(cls) -> bool:
            return True


    obj = MozzarellaCheese()
    print(f"Am I dairy? {obj.is_dairy()}")
