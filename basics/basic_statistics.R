# R Practice Sheet for statistics without the BS
library(graphics)
# Using R norm to generate a hundred points and plot in a histogram
random_points = rnorm(n=100, mean = 0, sd = 1)
histogram_100 = hist(random_points)

random_points_500 = rnorm(n=500, mean = 0, sd = 1)
histogram_500 = hist(random_points_500)

random_points_1000 = rnorm(n = 1000, mean = 0, sd = 1)
histogram_1000 = hist(random_points_1000)

random_points_10000 = rnorm(n=10000, mean = 0, sd = 1)
histogram_10000 = hist(random_points_10000, 
                       main = "Histogram of 10000 random samples from a Normal Distribution 
                       of Mean 1 and Standard Deviation 1",
                       xlab = "Sample value", # x axis label
                       ylab = "Frequency", # y axis label
                       border = "blue", # border color of bins
                       col = "green", # color inside bins
                       las = 1, # axis label orientation
                       prob = TRUE) # in frequency or probability

# using dnorm to draw the density curve
x <- seq(-4, 4, 0.01)
hist(random_points_10000, prob=TRUE)
curve(dnorm(x, mean=0, sd=1),add=TRUE) # add the curve, dnorm sets the probability of the numbers in the sequence given mean 0 and sd 1

# using pnorm to see the cumulative sum
histogram_cum_sum = hist(random_points_10000, 
                         xlab = "Sample value", # x axis label
                         ylab = "Frequency", # y axis label
                         border = "blue", # border color of bins
                         col = "green", # color inside bins
                         las = 1, # axis label orientation
                         prob = TRUE) # in frequency or probability
histogram_cum_sum$counts = cumsum(histogram_cum_sum$counts) # adjust the list of counts in each bin to be the cumulative sum
plot(x = histogram_cum_sum$breaks, y=histogram_cum_sum$density) # plot the adjusted histogram after counts adjustment to get cumulative histogram
curve(pnorm(x, mean=0, sd=1),add=TRUE) # pnorm the previous x sequence