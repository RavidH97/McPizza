from Entities.Ingredients.Cheese.Cheese import Cheese


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


# Example usage
if __name__ == "__main__":

    obj = MozzarellaCheese()
    print(f"Am I dairy? {obj.is_dairy()}")
