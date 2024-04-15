from Entities.Pizza import Pizza
from Entities.Queues.BaseQueue import BaseQueue


class PutInOvenQueue(BaseQueue[Pizza]):
    """Singleton FIFO put in oven queue for pizzas."""
    _class_name = "Put In Oven Queue"

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name
