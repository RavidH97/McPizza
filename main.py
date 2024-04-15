import random
import threading
import time
from Entities.OrderFactory import OrderFactory
from Entities.Queues.OrderQueue import OrderQueue
from Entities.Queues.PutInOvenQueue import PutInOvenQueue
from Entities.Queues.ReadyPizzaQueue import ReadyPizzaQueue
from Entities.Queues.PullFromOvenQueue import PullFromOvenQueue
from Entities.Oven import Oven
from Entities.Worker import Worker


def setup_queues():
    """Set up relevant queue instances."""
    OrderQueue.get_instance()
    PutInOvenQueue.get_instance()
    ReadyPizzaQueue.get_instance()
    PullFromOvenQueue.get_instance()


def create_ovens(num_ovens):
    """Create several Oven instances."""
    for _ in range(num_ovens):
        Oven()


def create_workers(num_workers, end_of_time):
    """Create several Worker instances."""
    for i in range(num_workers):
        worker = Worker(str(i), end_of_time)
        worker.start()


def run_order_factory(num_orders, interval_min, interval_max):
    """Create one Order Factory and make it create new orders."""
    order_factory = OrderFactory.get_instance()
    for _ in range(num_orders):
        order_factory.create_pizza()
        interval = random.uniform(interval_min, interval_max)
        time.sleep(interval)


def main():
    setup_queues()
    num_ovens = 2
    num_workers = 4
    num_orders = 5
    interval_min = 1
    interval_max = 2
    end_of_time = threading.Event()
    create_ovens(num_ovens)
    create_workers(num_workers, end_of_time)

    # Start the order factory thread
    order_factory_thread = threading.Thread(target=run_order_factory, args=(num_orders, interval_min, interval_max))
    order_factory_thread.start()

    # Wait for the order factory to finish creating orders
    order_factory_thread.join()

    # Wait for all pizzas to be ready
    while ReadyPizzaQueue.get_instance().qsize() < num_orders:
        time.sleep(1)

    # Stop all worker threads
    end_of_time.set()
    for thread in threading.enumerate():
        if isinstance(thread, Worker):
            thread.join()

    print("All pizzas are ready!")


if __name__ == "__main__":
    main()
