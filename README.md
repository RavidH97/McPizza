Pizza Ordering System

This is a simple pizza ordering system implemented in Python. It consists of several components:

Pizza: Represents a pizza with various ingredients such as dough, sauces, cheeses, and toppings.
Order Factory: A function that creates new pizza instances and publishes them to the order queue.
Worker: A component that consumes orders from the order queue, prepares the pizzas, and publishes them to the put-in-oven queue.

Installation
Clone the repository to your local machine.
Ensure you have Python 3.10 installed.

Usage
Run the main.py script to start the pizza ordering system.
The system will automatically create ovens, workers, and an order factory.
New orders will be created and processed in real-time.
Once all orders have been processed, the program will exit gracefully.

Configuration
You can customize the behavior of the system by adjusting parameters such as the number of ovens, workers, and orders, as well as the intervals for order creation.