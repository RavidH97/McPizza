import threading
import uuid
import time
from threading import Thread, Lock
from Entities.Entity import Entity
from Entities.Pizza import Pizza
from Entities.Queues.PullFromOvenQueue import PullFromOvenQueue
from Util.Exceptions.OvenException import OvenException
from Util.Exceptions.StatusException import StatusException
from Util.PizzaStatus import PizzaStatus


class Oven(Entity):
    """Oven class to bake pizzas and manage the baking process."""

    _class_name = "Oven"
    _ovens = {}
    _lock = Lock()

    def __init__(self):
        self.oven_id = uuid.uuid4()
        self._current_pizza = None
        self.pull_from_oven_queue = PullFromOvenQueue.get_instance()
        self._pull_lock = Lock()
        self._bake_lock = Lock()
        self._bake_time = 0
        super().__init__()

        with Oven._lock:
            Oven._ovens[self.oven_id] = self

    @classmethod
    def get_oven_by_id(cls, oven_id: uuid.UUID) -> 'Oven':
        """Get the oven instance by its ID."""
        with cls._lock:
            return cls._ovens.get(oven_id)

    @classmethod
    def has_vacant_oven(cls) -> bool:
        """Check if there is a vacant oven."""
        with cls._lock:
            return any(oven.get_current_pizza() is None for oven in cls._ovens.values())

    @classmethod
    def get_next_vacant_oven(cls) -> 'Oven':
        """Get the next vacant oven."""
        with cls._lock:
            for oven in cls._ovens.values():
                if oven.get_current_pizza() is None:
                    return oven

    def bake_thread(self):
        """Bake pizza action."""
        self._log(f"Baking pizza: {self._current_pizza.pizza_id}")
        time.sleep(self._bake_time)
        try:
            self._current_pizza.bake_pizza()
            self.pull_from_oven_queue.put(self.oven_id)
            self._log(f"Pizza {self._current_pizza.pizza_id} is baked!")
        except StatusException as se:
            self._log(str(se))

    def bake_pizza(self, pizza: Pizza, bake_time: float):
        """Bake a pizza if the oven is clear."""
        with self._bake_lock:
            if self._current_pizza is not None:
                raise RuntimeError("Another pizza is already being baked.")
            self._current_pizza = pizza
            self._bake_time = bake_time
        threading.Thread(target=self.bake_thread).start()

    def pull_pizza_from_oven(self) -> Pizza:
        """Pull the pizza from the oven."""
        with self._pull_lock:
            if self._current_pizza is None:
                raise OvenException("No pizza is currently in the oven")
            pizza = self._current_pizza
            self._current_pizza = None
            self._log(f"Oven is ready for a new pizza.")
            return pizza

    def get_current_pizza(self) -> Pizza:
        return self._current_pizza

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name + " " + str(self.oven_id)

