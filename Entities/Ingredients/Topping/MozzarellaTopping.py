from Entities.Ingredients.Topping.Topping import Topping


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


# Example usage
if __name__ == "__main__":

    obj = MozzarellaTopping()
    print(f"Am I dairy? {obj.is_dairy()}")
