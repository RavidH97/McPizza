from Entities.Ingredients.Topping.Topping import Topping


class MushroomTopping(Topping):
    """Mushroom Topping class"""

    _class_name = "Mushroom Topping"

    @classmethod
    def get_name(cls) -> str:
        return cls._class_name

    @classmethod
    def is_vegan(cls) -> bool:
        return True

    @classmethod
    def is_dairy(cls) -> bool:
        return False


# Example usage
if __name__ == "__main__":

    obj = MushroomTopping()
    print(f"Am I dairy? {obj.is_dairy()}")
