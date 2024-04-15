from Entities.Pizza import Pizza
from Entities.Queues.BaseQueue import BaseQueue


class ReadyPizzaQueue(BaseQueue[Pizza]):
    """Singleton FIFO order queue for pizzas."""
    _class_name = "Ready Pizza Queue"

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name
