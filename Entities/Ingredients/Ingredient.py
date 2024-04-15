from abc import abstractmethod
from Entities.Entity import Entity


class Ingredient(Entity):
    """Ingredient model."""

    _class_name = "Ingredient"

    def __init__(self):
        """Initialize Ingredient."""
        super().__init__()

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self):
        return self.class_name()

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Gets ingredient name."""
        pass

    @classmethod
    @abstractmethod
    def is_vegan(cls) -> bool:
        """Is the ingredient vegan?"""
        pass

    @classmethod
    @abstractmethod
    def is_dairy(cls) -> bool:
        """Is the ingredient dairy?"""
        pass


# Example usage
if __name__ == "__main__":
    class Pepperoni(Ingredient):
        """Pepperoni class"""
        _class_name = "Pepperoni"

        def __init__(self):
            """Initialize Pepperoni."""
            super().__init__()

        @classmethod
        def get_name(cls) -> str:
            return cls._class_name

        @classmethod
        def is_vegan(cls) -> bool:
            return False

        @classmethod
        def is_dairy(cls) -> bool:
            return False

    obj = Pepperoni()
    print(f"Am I vegan? {obj.is_vegan()}")
