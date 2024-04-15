from Entities.Pizza import Pizza
from Entities.Queues.BaseQueue import BaseQueue


class OrderQueue(BaseQueue[Pizza]):
    """Singleton FIFO order queue for pizzas."""
    _class_name = "Order Queue"

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name
