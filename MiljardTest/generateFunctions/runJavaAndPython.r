# Number of times to run
num_runs <- 1000

# Argument to pass to the Java program
arg <- "1"

# Directory containing Main.class
class_path <- "/home/burk/LTH/UAPprojekt/test/MiljardTest/testFunctions"

# Run Main with the argument
for (i in 1:num_runs) {
  cat(sprintf("Run %d - Java\n", i))
  system(sprintf("java -cp %s Main %s", class_path, arg))
}
