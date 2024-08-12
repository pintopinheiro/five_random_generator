"""Entity Model to generate numbers."""
import random


def generate_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    return random_numbers
