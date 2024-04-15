import time
from threading import Thread, Lock

from Entities.Ingredients.Dough.WheatDough import WheatDough
from Entities.Queues.PullFromOvenQueue import PullFromOvenQueue
from Entities.Queues.PutInOvenQueue import PutInOvenQueue
from Entities.Queues.OrderQueue import OrderQueue
from Entities.Queues.ReadyPizzaQueue import ReadyPizzaQueue
from Entities.Oven import Oven
from Entities.Entity import Entity
from Util.Exceptions.OvenException import OvenException
from Util.Exceptions.StatusException import StatusException


class Worker(Entity, Thread):
    """Worker class to perform actions according to the given algorithm."""
    _class_name = "Worker"
    _pull_from_oven_lock = Lock()
    _put_in_oven_lock = Lock()
    _get_order_lock = Lock()
    _default_dough_class = WheatDough

    def __init__(self, name, end_of_time_event):
        """Init the worker"""
        Thread.__init__(self)
        self._name = name
        self.pull_from_oven_queue = PullFromOvenQueue.get_instance()
        self.put_in_oven_queue = PutInOvenQueue.get_instance()
        self.order_queue = OrderQueue.get_instance()
        self.ready_pizza_queue = ReadyPizzaQueue.get_instance()
        self._end_of_time = end_of_time_event
        super().__init__()

    def run(self):
        """Make the worker work until his shift is over"""
        self._log("Work work work work work work")
        while not self._end_of_time.is_set():
            if not self.pull_from_oven():
                if not self.put_in_oven():
                    self.prepare_pizza()

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name + " " + self._name

    def pull_from_oven(self) -> bool:
        """Pull pizza from an oven, return True if succeeded, False otherwise"""
        with self._pull_from_oven_lock:
            if not self.pull_from_oven_queue.empty():
                self._log("Pulling a pizza from the oven")
                oven_id = self.pull_from_oven_queue.get()
                oven = Oven.get_oven_by_id(oven_id)
                baked_pizza = oven.pull_pizza_from_oven()
            else:
                return False
        self.ready_pizza_queue.put(baked_pizza)
        self._log(f"Pizza {baked_pizza.pizza_id} is ready!")
        return True

    def put_in_oven(self) -> bool:
        """Put pizza in an oven, return True if succeeded, False otherwise"""
        with self._put_in_oven_lock:
            try:
                if not self.put_in_oven_queue.empty() and Oven.has_vacant_oven():
                    pizza = self.put_in_oven_queue.get()
                    self._log(f"Putting pizza {pizza.pizza_id} in the oven")
                    oven = Oven.get_next_vacant_oven()
                    oven.bake_pizza(pizza, 5)
                else:
                    return False
            except OvenException as oe:
                self._log(str(oe))
                return False
        return True

    def prepare_pizza(self) -> bool:
        """Prepare pizza, return True if succeeded, False otherwise"""
        with self._get_order_lock:
            if not self.order_queue.empty():
                self._log("Preparing a pizza")
                pizza = self.order_queue.get()
            else:
                return False
        time.sleep(2)
        try:
            if pizza.dough is None:
                pizza.dough = self._default_dough_class()
            pizza.prepare_pizza()
            self.put_in_oven_queue.put(pizza)
            self._log(f"Finished preparing pizza {pizza.pizza_id}")
        except StatusException as se:
            self._log(str(se))
            return False
        return True
