import time

LOOP_ITERATIONS = 10**6
ITERATIONS = 1000

input = "data/in/data1.txt"

emptyLoopOutput = "data/outPython/data1_emptyLoop_out.txt"
arithmeticOutput = "data/outPython/data1_arithmetic_out.txt"
sortOutput = "data/outPython/data1_sort_out.txt"

def testEmptyLoop(output, magnitude, n):
    """
    This function runs a loop for a given magnitude and does nothing in the loop.
    It is used to test the performance of an empty loop.
    """
    # Clear the output file before starting
    open(output, 'w').close()
    sum = 0

    for j in range(n):

        start_time = time.time()
        for i in range(1, magnitude):
            pass #Do nothing
        end_time = time.time()

        duration = end_time - start_time
        sum += duration

        # Write the duration to the output file
        with open(output, 'a') as out_file:
            out_file.write(f"{duration:.6f}\n")  # 6 decimal places
    
    return sum

def testArithmeticLoop(output, magnitude, n):
    """
    This function runs a loop for a given magnitude and performs an arithmetic operation in the loop.
    It is used to test the performance of a loop with arithmetic operations.
    """
    # Clear the output file before starting
    open(output, 'w').close()

    sum = 0
    timeSum = 0
    for j in range(n):

        start_time = time.time()
        for i in range(1, magnitude):
            sum = sum + i
        end_time = time.time()

        duration = end_time - start_time
        timeSum += duration

        # Write the duration to the output file
        with open(output, 'a') as out_file:
            out_file.write(f"{duration:.6f}\n")
    
    print("Sum:", sum)

    return timeSum

def testSort(input, output, n):
    """
    This function reads numbers from a file, stores them in a list, and sorts them.
    It is used to test the performance of sorting algorithms.
    """
    numbers = []
    with open(input, 'r') as file:
        for line in file:
            numbers.append(int(line.strip()))

    # Clear the output file before starting
    open(output, 'w').close()
    timeSum = 0

    for i in range(n):
        # Create a copy of the list to sort
        sortedList = numbers.copy()

        start_time = time.time()
        sortedList.sort()
        end_time = time.time()
        
        duration = end_time - start_time
        timeSum += duration

        # Write the duration to the output file
        with open(output, 'a') as out_file:
            out_file.write(f"{duration:.6f}\n")  # 6 decimal places

       
    return timeSum
    
timeTest = testEmptyLoop(emptyLoopOutput ,LOOP_ITERATIONS, ITERATIONS)
print("Test: Empty Loop",timeTest, "seconds")

timeTest = testArithmeticLoop(arithmeticOutput, LOOP_ITERATIONS, ITERATIONS)
print("Test: Arithmetic Loop",timeTest, "seconds")

timeTest = testSort(input, sortOutput, ITERATIONS)
print("Test: Sort",timeTest, "seconds")


