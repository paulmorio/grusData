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
                       prob= FALSE) # in frequency or probability

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
plot(histogram_cum_sum) # plot the adjusted histogram after counts adjustment to get cumulative histogram
curve(pnorm(x, mean=0, sd=1), add = TRUE) # pnorm the previous x sequence

## Simple empirical plots of the distributions themselves
#Exponential
interval.exp<-seq(0, 10, 0.01)
plot(interval.exp,dexp(interval.exp,rate=0.5))
lines(interval.exp,dexp(interval.exp,rate=1),col="red")
lines(interval.exp,dexp(interval.exp,rate=2),col="blue")
lines(interval.exp,dexp(interval.exp,rate=10),col="green")

#Gamma
interval.gamma<-seq(0, 20, 0.01)
plot(interval.gamma,dgamma(interval.gamma,shape=1,scale=2))
lines(interval.gamma,dgamma(interval.gamma,shape=2,scale=2),col="red")
lines(interval.gamma,dgamma(interval.gamma,shape=5,scale=2),col="blue")
lines(interval.gamma,dgamma(interval.gamma,shape=5,scale=0.5),col="green")


#Student
interval.t<-seq(-10,10, 0.01)
plot(interval.t,dt(interval.t,10))
lines(interval.t,dt(interval.t,5),col="red")
lines(interval.t,dt(interval.t,2),col="blue")
lines(interval.t,dt(interval.t,1),col="green")

## Simple empirical plots of the cumulative distributions (ECDF)
#Exponential
interval.exp<-seq(0, 10, 0.01)
plot(interval.exp,pexp(interval.exp,rate=0.5))
lines(interval.exp,pexp(interval.exp,rate=1),col="red")
lines(interval.exp,pexp(interval.exp,rate=2),col="blue")
lines(interval.exp,pexp(interval.exp,rate=10),col="green")

#Gamma
interval.gamma<-seq(0, 20, 0.01)
plot(interval.gamma,pgamma(interval.gamma,shape=1,scale=2))
lines(interval.gamma,pgamma(interval.gamma,shape=2,scale=2),col="red")
lines(interval.gamma,pgamma(interval.gamma,shape=5,scale=2),col="blue")
lines(interval.gamma,pgamma(interval.gamma,shape=5,scale=0.5),col="green")

#Student
interval.t<-seq(-10,10, 0.01)
plot(interval.t,pt(interval.t,10))
lines(interval.t,pt(interval.t,5),col="red")
lines(interval.t,pt(interval.t,2),col="blue")
lines(interval.t,pt(interval.t,1),col="green")