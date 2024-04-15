from uuid import UUID
from Entities.Queues.BaseQueue import BaseQueue


class PullFromOvenQueue(BaseQueue[UUID]):
    """Singleton FIFO queue for pulling pizzas from the oven."""
    _class_name = "Pull From Oven Queue"

    @classmethod
    def class_name(cls) -> str:
        return cls._class_name

    @property
    def entity_name(self) -> str:
        return self._class_name
