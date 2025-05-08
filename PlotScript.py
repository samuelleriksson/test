import matplotlib.pyplot as plt

python_emptyLoop_data = "data/outPython/data1_emptyLoop_out.txt"
python_arithmetic_data = "data/outPython/data1_arithmetic_out.txt"
python_sort_data = "data/outPython/data1_sort_out.txt"
java_emptyLoop_data = "data/outJava/data1_emptyLoop_out.txt"
java_arithmetic_data = "data/outJava/data1_arithmetic_out.txt"
java_sort_data = "data/outJava/data1_sort_out.txt"

with open(python_emptyLoop_data, "r") as file:
    python_emptyLoop_list = [float(line.strip()) for line in file.readlines()]

with open(python_arithmetic_data, "r") as file:
    python_arithmetic_list = [float(line.strip()) for line in file.readlines()]

with open(python_sort_data, "r") as file:
    python_sort_list = [float(line.strip()) for line in file.readlines()]


with open(java_emptyLoop_data, "r") as file:
    java_emptyLoop_list = [float(line.strip()) for line in file.readlines()]

with open(java_arithmetic_data, "r") as file:
    java_arithmetic_list = [float(line.strip()) for line in file.readlines()]

with open(java_sort_data, "r") as file:
    java_sort_list = [float(line.strip()) for line in file.readlines()]

# Convert Java data from nanoseconds to seconds for consistency
java_emptyLoop_list = [x / 1e9 for x in java_emptyLoop_list]
java_arithmetic_list = [x / 1e9 for x in java_arithmetic_list]
java_sort_list = [x / 1e9 for x in java_sort_list]

# Create a separate plot for Python data
plt.figure()
plt.plot(python_emptyLoop_list, label="Python Empty Loop")
plt.plot(python_arithmetic_list, label="Python Arithmetic")
plt.plot(python_sort_list, label="Python Sort")
plt.xlabel("Iterations")
plt.ylabel("Time (seconds)")
plt.title("Python Performance Comparison")
plt.legend()
plt.grid()


plt.show()

# Create a separate plot for Java data
plt.figure()
plt.plot(java_emptyLoop_list, label="Java Empty Loop")
plt.plot(java_arithmetic_list, label="Java Arithmetic")
plt.plot(java_sort_list, label="Java Sort")
plt.xlabel("Iterations")
plt.ylabel("Time (seconds)")
plt.title("Java Performance Comparison")
plt.legend()
plt.grid()
plt.show()

