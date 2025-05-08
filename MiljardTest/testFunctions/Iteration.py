import time

iterationNbr = 1000000000;

def iteration(n):
    t1 = time.time()
    for i in range(10**9): 
        pass # gör ingenting
    t2 = time.time() - t1
    return t2

def arithmetic(n):
    tot = 0
    t1 = time.time()
    for i in range(10**9): 
        tot += i * 2 / 3
    t2 = time.time() - t1
    return t2

def timsort(l):
    t1 = time.time()
    l.sort()
    t2 = time.time() - t1
    return t2

# Function to read integers from a file and return them as a list
def read_integers_from_file(file_path):
    numbers = []
    
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Parse each line as an integer and add to the list
                numbers.append(int(line.strip()))  # .strip() removes leading/trailing whitespace
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    
    return numbers

# Main part of the script
if __name__ == "__main__":
    # Path to the file containing integers
    file_path = "/home/christiant14/LTH/UAPprojekt/MiljardTest/dataInAndOut/dataIn/RandomInts.txt"
    
    # Read integers from the file
    numbers = read_integers_from_file(file_path)
    
    # Sort the list using Python's built-in Timsort
    numbers.sort()  # Sorts in-place using Timsort
    
    # Print the first 10 numbers for verification (optional)
    print("First 10 numbers:", numbers[:10])

    # Optionally, print the size of the list to confirm all numbers were read
    print("Total numbers read:", len(numbers))



#r1 = iteration(iterationNbr)
#r2 = arithmetic(iterationNbr)
l1 = read_integers_from_file("dataInAndOut/dataIn/RandomInts.txt")
r3 = timsort(l1)
print(r3)

#print(r1)
#print(r2)
