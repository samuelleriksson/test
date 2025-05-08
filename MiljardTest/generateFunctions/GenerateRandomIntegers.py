import random

with open("/home/christiant14/LTH/UAPprojekt/MiljardTest/dataInAndOut/dataIn/RandomInts.txt", "w") as f: #ändra om det behövs, måste vara i rätt path beroende åp vilken dator osm används.
    for i in range(1_000_000):
        f.write(f"{random.randint(0, 1_000_000)}\n")
