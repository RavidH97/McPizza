from Entities.Ingredients.Dough.Dough import Dough


class WheatDough(Dough):
    """Wheat Dough class"""

    _class_name = "Wheat Dough"

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
        return "Wheat"


# Example usage
if __name__ == "__main__":
    obj = WheatDough()
    print(f"Am I vegan? {obj.is_vegan()}")
