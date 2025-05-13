setwd("/Users/samuel/Documents/UAP/test/V1Concept/")

java_sort <- read.table("data/outJava/data1_sort_out.txt", header = FALSE)
java_empty_loop <- read.table("data/outJava/data1_emptyLoop_out.txt", header = FALSE)
java_arithmetic <- read.table("data/outJava/data1_arithmetic_out.txt", header = FALSE)

python_sort <- read.table("data/outPython/data1_sort_out.txt", header = FALSE)
python_empty_loop <- read.table("data/outPython/data1_emptyLoop_out.txt", header = FALSE)
python_arithmetic <- read.table("data/outPython/data1_arithmetic_out.txt", header = FALSE)


plot(java_sort$V1,type = "l",col = "blue", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Java Sort")
plot(java_empty_loop$V1,type = "l", col = "red", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Java Empty Loop")
plot(java_arithmetic$V1,type = "l", col = "green", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Java Arithmetic")

plot(python_sort$V1, type = "l", col = "red", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Python Sort")

plot(python_empty_loop$V1,type = "l", col = "grey", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Python Empty Loop")
plot(python_arithmetic$V1,type = "l", col = "yellow", lwd = 2,
     ylab = "Values", xlab = "Index", main = "Python Arithmetic")


# Define a helper function to summarize a dataset
summarize_data <- function(data) {
  values <- data[[1]]
  c(
    Mean = mean(values),
    Median = median(values),
    SD = sd(values),
    Min = min(values),
    Max = max(values)
  )
}

# Apply the function to each dataset
summary_table <- data.frame(
  Dataset = c(
    "java_empty_loop", "python_empty_loop", "java_sort", "python_sort", "java_arithmetic",
    "python_arithmetic"),
  rbind(
    summarize_data(java_empty_loop),
    summarize_data(python_empty_loop),
    summarize_data(java_sort),
    summarize_data(python_sort),
    summarize_data(java_arithmetic),
    summarize_data(python_arithmetic)
  )
)

# Show the table
summary_table


# Perform t-tests
t_empty <- t.test(java_empty_loop[[1]], python_empty_loop[[1]])
t_sort <- t.test(java_sort[[1]], python_sort[[1]])
t_arith <- t.test(java_arithmetic[[1]], python_arithmetic[[1]])

t_test_results <- data.frame(
  Comparison = c("Empty loop", "Sort", "Arithmetic"),
  P_value = signif(c(
    t.test(java_empty_loop[[1]], python_empty_loop[[1]])$p.value,
    t.test(java_sort[[1]], python_sort[[1]])$p.value,
    t.test(java_arithmetic[[1]], python_arithmetic[[1]])$p.value
  ), 3),
  
  Java_mean_sec = round(c(
    mean(java_empty_loop[[1]]),
    mean(java_sort[[1]]),
    mean(java_arithmetic[[1]])
  ) / 1e9, 6),
  
  Python_mean_sec = round(c(
    mean(python_empty_loop[[1]]),
    mean(python_sort[[1]]),
    mean(python_arithmetic[[1]])
  ), 6)
)

t_test_results


