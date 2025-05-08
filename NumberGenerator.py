import random

with open("data/in/data1.txt", "w") as f:
    for _ in range(100_000):
        f.write(f"{random.randint(0, 100_000)}\n")
