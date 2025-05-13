import time
import sys

iterationNbr = 1000000000

def iteration(n):
    t1 = time.time_ns()
    for i in range(10**9): 
        pass # gör ingenting
    t2 = time.time_ns() - t1
    return t2

def arithmetic(n):
    tot = 0
    t1 = time.time_ns()
    for i in range(10**9): 
        tot += i * 2 / 3
    t2 = time.time_ns() - t1
    return t2

def timsort(l):
    t1 = time.time_ns()
    l.sort()
    t2 = time.time_ns() - t1
    return t2


def readIntegersFromFile(file_path):
    numbers = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                numbers.append(int(line.strip())) 
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    return numbers



def writeToFile(file_path, value):
    try:
        with open(file_path, "a") as file:  # 'a' for append mode
            file.write(f"{value}\n")   # write the float as a new line
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")



if len(sys.argv) > 1: #som switch sats i java, tar args från CLI så att det är lätt att koda i R
    match sys.argv[1]:
        case "1":
            r1 = iteration(iterationNbr)
            writeToFile("MiljardTest/dataInAndOut/dataOut/pythonIterationData.txt", r1)
        case "2":
            r2 = arithmetic(iterationNbr)
            writeToFile("MiljardTest/dataInAndOut/dataOut/pythonArithmeticData.txt", r2)
        case "3":
            l1 = readIntegersFromFile("MiljardTest/dataInAndOut/dataIn/RandomInts.txt")
            r3 = timsort(l1)
            writeToFile("MiljardTest/dataInAndOut/dataOut/pythonSortData.txt", r3)
        case _:
            print("Unknown argument")
else:
    print("no arg")


