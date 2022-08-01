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



#outliers
install.packages("outliers")
library(outliers)

test <- grubbs.test(book1_txt$salary)
test

#histogram
hist(salary,xlab = "salary",col="maroon",border="Black")

hist(IBM_Marks$Total,xlab="Total",col="Yellow",border="black")


#BarChart
barplot(IBM_Marks$Total,xlab="Total",col="maroon",border="black")

#Pie chart
pie(book1_txt$salary)