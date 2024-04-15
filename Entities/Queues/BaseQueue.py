import queue
from abc import ABC
from threading import Lock
from typing import TypeVar, Generic
from Entities.Entity import Entity

T = TypeVar('T')


class BaseQueue(Generic[T], Entity, ABC):
    """Base class for thread-safe FIFO queues."""

    _instance = None
    _lock = Lock()

    def __init__(self):
        super().__init__()
        self._queue = None

    @classmethod
    def get_instance(cls):
        """Return the singleton instance of the queue."""
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        """Create a new instance of the queue."""
        instance = super().__new__(cls)
        instance._queue = queue.Queue()
        return instance

    def put(self, item: T):
        """Put an item into the queue."""
        self._queue.put(item)

    def get(self) -> T:
        """Get the next item from the queue."""
        return self._queue.get()

    def empty(self) -> bool:
        return self._queue.empty()

    def qsize(self) -> int:
        return self._queue.qsize()
