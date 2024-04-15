from Entities.Ingredients.Cheese.Cheese import Cheese


class CashewCheese(Cheese):
    """Cashew Cheese class"""

    _class_name = "Cashew Cheese"

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

    obj = CashewCheese()
    print(f"Am I dairy? {obj.is_dairy()}")
