from abc import ABC
from Entities.Ingredients.Ingredient import Ingredient


class Topping(Ingredient, ABC):
    """Topping class"""
    _class_name = "Topping"

    def __init__(self):
        """Initialize Topping."""
        super().__init__()


# Example usage
if __name__ == "__main__":
    class MozzarellaTopping(Topping):
        """Mozzarella Topping class"""

        _class_name = "Mozzarella Topping"

        @classmethod
        def get_name(cls) -> str:
            return cls._class_name

        @classmethod
        def is_vegan(cls) -> bool:
            return False

        @classmethod
        def is_dairy(cls) -> bool:
            return True


    obj = MozzarellaTopping()
    print(f"Am I dairy? {obj.is_dairy()}")
