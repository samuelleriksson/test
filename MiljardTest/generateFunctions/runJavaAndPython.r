# Number of times to run
num_runs <- 250

# Argument to pass
arg <- "1"

# Paths
class_path <- "/Users/samuel/Documents/UAP/test/MiljardTest/testFunctions/"
python_path <- "/Users/samuel/Documents/UAP/test/MiljardTest/testFunctions/Main.py"

# Run Java
for (i in 1:num_runs) {
  cat(sprintf("Run %d - Java\n", i))
  system(sprintf("java -cp \"%s\" Main %s", class_path, arg))
}

# Run Python
for (i in 1:num_runs) {
  cat(sprintf("Run %d - Python\n", i))
  system(sprintf("python3 \"%s\" %s", python_path, arg))
}
