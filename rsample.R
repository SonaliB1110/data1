m <- c(2, 3, 7, 8, 10, 13, 14, 15,
       18, 18, 20, 26, 25, 26, 27, 28)
hist(m)
l <- c(2, 3, 7, 8, 10, 13, 14, 15,
       18, 18, 20, 26, 25, 26, 27, 28)

# Mean of l
mean <- mean(l)

# Plotting histogram and Adding
# Mean line to Histogram
hist(l)
abline(v = mean, col = 'blue')

