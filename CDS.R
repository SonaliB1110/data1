#Mean
mean = mean(IBM_Marks$Total)
print(mean)
#Median
median = mean(IBM_Marks$Total)
print(median)
#Mode
install.packages("modeest")
library(modeest)
mlv(IBM_Marks$Total,method="mfv")
#Quantile
d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.50))

d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.75))

d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.25))

#MinMax
min(d)
max(d)

#Range
range(d)
print(max(d)-min(d))

#variance
var(IBM_Marks$Total)


#Inter Quantile Range
IQR(d)

#standard deviation
sd(IBM_Marks$Total)

#BoxPlot
boxplot(IBM_Marks$Total,horizontal = TRUE)


#skewness
install.packages("moments")
library(moments)

skewness(IBM_Marks$Total)


#Boxplot
boxplot(book1_txt$salary,horizontal = TRUE)


#scatterplot3d
install.packages("scatterplot3d")
library(scatterplot3d)
attach(book1_txt)
scatterplot3d(salary,start_date,main="scatter_plot",xlab="salary",ylab = "start_date",zlab="dept",pch=18)



#scatterplot
attach(book1_txt)
plot(salary,start_date,main="scatter_plot",xlab="salary",ylab = "start_date",pch=18)


pie(book1_txt$salary)

