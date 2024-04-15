import uuid
from enum import Enum
from typing import Optional, List, Type
from Entities.Entity import Entity
from Entities.Ingredients.Cheese.CashewCheese import CashewCheese
from Entities.Ingredients.Cheese.Cheese import Cheese
from Entities.Ingredients.Cheese.MozzarellaCheese import MozzarellaCheese
from Entities.Ingredients.Dough import Dough
from Entities.Ingredients.Dough.CornDough import CornDough
from Entities.Ingredients.Dough.WheatDough import WheatDough
from Entities.Ingredients.Sauce.Sauce import Sauce
from Entities.Ingredients.Sauce.CreamSauce import CreamSauce
from Entities.Ingredients.Sauce.TomatoSauce import TomatoSauce
from Entities.Ingredients.Topping.Topping import Topping
from Entities.Ingredients.Topping.MushroomTopping import MushroomTopping
from Entities.Ingredients.Topping.PepperoniTopping import PepperoniTopping
from Util.Exceptions.StatusException import StatusException
from Util.PizzaStatus import PizzaStatus


class Pizza(Entity):
    """Pizza model."""

    _class_name = "Pizza"

    def __init__(self,
                 dough: Dough,
                 sauces: Optional[List[Sauce]] = None,
                 cheeses: Optional[List[Cheese]] = None,
                 toppings: Optional[List[Topping]] = None):
        """Init Pizza model."""
        self.pizza_id = uuid.uuid4()
        self._status = PizzaStatus.UNPREPARED
        self.dough = dough
        self.sauces = sauces if sauces is not None else []
        self.cheeses = cheeses if cheeses is not None else []
        self.toppings = toppings if toppings is not None else []
        super().__init__()

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name + " " + str(self.pizza_id)

    @property
    def get_status(self) -> PizzaStatus:
        return self._status

    def is_baked(self) -> bool:
        return self._status is PizzaStatus.BAKED

    def prepare_pizza(self):
        """Prepare pizza"""
        if self._status == PizzaStatus.UNPREPARED:
            self._status = PizzaStatus.UNBAKED
            self._log("I'm prepared!")
        else:
            raise StatusException("Could not prepare pizza :(")

    def bake_pizza(self):
        """Bake pizza"""
        if self._status == PizzaStatus.UNBAKED:
            self._status = PizzaStatus.BAKED
            self._log("I'm baked!")
        else:
            raise StatusException("Could not bake pizza :(")


# Example usage
if __name__ == "__main__":
    happy_pizza = Pizza(WheatDough(),
                        [CreamSauce()],
                        [MozzarellaCheese()],
                        [PepperoniTopping(), PepperoniTopping(), MushroomTopping()])
    happy_pizza.prepare_pizza()
    happy_pizza.bake_pizza()

    sad_pizza = Pizza(CornDough(),
                      [TomatoSauce()],
                      [CashewCheese()])
    sad_pizza.prepare_pizza()
    sad_pizza.bake_pizza()
