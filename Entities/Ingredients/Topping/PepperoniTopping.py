from Entities.Ingredients.Topping.Topping import Topping


class PepperoniTopping(Topping):
    """Pepperoni Topping class"""

    _class_name = "Pepperoni Topping"

    @classmethod
    def get_name(cls) -> str:
        return cls._class_name

    @classmethod
    def is_vegan(cls) -> bool:
        return False

    @classmethod
    def is_dairy(cls) -> bool:
        return False


# Example usage
if __name__ == "__main__":

    obj = PepperoniTopping()
    print(f"Am I dairy? {obj.is_dairy()}")
