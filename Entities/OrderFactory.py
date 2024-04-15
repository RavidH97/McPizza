import random
from threading import Lock
from Entities.Entity import Entity
from Entities.Ingredients.Cheese.CashewCheese import CashewCheese
from Entities.Ingredients.Cheese.MozzarellaCheese import MozzarellaCheese
from Entities.Ingredients.Dough.CornDough import CornDough
from Entities.Ingredients.Dough.WheatDough import WheatDough
from Entities.Ingredients.Sauce.CreamSauce import CreamSauce
from Entities.Ingredients.Sauce.TomatoSauce import TomatoSauce
from Entities.Ingredients.Topping.MozzarellaTopping import MozzarellaTopping
from Entities.Ingredients.Topping.MushroomTopping import MushroomTopping
from Entities.Ingredients.Topping.PepperoniTopping import PepperoniTopping
from Entities.Pizza import Pizza
from Entities.Queues.OrderQueue import OrderQueue


class OrderFactory(Entity):
    """Singleton Order factory class for creating pizzas."""

    _instance = None
    _lock = Lock()

    _class_name = "Order Factory"

    def __init__(self):
        super().__init__()
        self.order_queue = None

    @classmethod
    def get_instance(cls):
        """Get order factory instance and create it if it does not exist yet"""
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance.order_queue = OrderQueue.get_instance()
        return cls._instance

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self.class_name()

    def create_pizza(self):
        """Creating a pizza instance and putting it in the order queue"""
        self._log("Creating random pizza")
        pizza = self.create_random_pizza()
        self._log(f"Insert pizza {pizza.pizza_id} to order queue")
        self._instance.order_queue.put(pizza)

    @classmethod
    def create_random_pizza(cls) -> Pizza:
        """Creates a random pizza with random dough, sauces, cheeses, and toppings."""
        dough = random.choice([CornDough(), WheatDough()])

        num_sauces = random.randint(0, 2)
        sauces = [random.choice([CreamSauce(), TomatoSauce()]) for _ in range(num_sauces)]

        num_cheeses = random.randint(0, 3)
        cheeses = [random.choice([CashewCheese(), MozzarellaCheese()]) for _ in range(num_cheeses)]

        num_toppings = random.randint(0, 5)
        toppings = [random.choice([MozzarellaTopping(), MushroomTopping(), PepperoniTopping()]) for _ in
                    range(num_toppings)]

        # Create and return the pizza
        return Pizza(dough, sauces, cheeses, toppings)


# example usage
if __name__ == "__main__":
    factory = OrderFactory.get_instance()
    factory.create_pizza()
