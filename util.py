import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)

def primo(start=2, end=100):
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num
