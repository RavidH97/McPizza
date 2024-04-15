from Entities.Ingredients.Sauce.Sauce import Sauce


class CreamSauce(Sauce):
    """Cream Sauce class"""

    _class_name = "Cream Sauce"

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

    obj = CreamSauce()
    print(f"Am I dairy? {obj.is_dairy()}")
