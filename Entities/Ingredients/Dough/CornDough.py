from Entities.Ingredients.Dough.Dough import Dough


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


# Example usage
if __name__ == "__main__":
    obj = CornDough()
    print(f"Am I vegan? {obj.is_vegan()}")
