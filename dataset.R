data<- read.csv("https://databank.worldbank.org/data/download/GDP.csv")
View(data)
data1<-read.delim("https://www.w3.org/TR/PNG/iso_8859-1.txt")
View(data1)
data2 <-read.delim("http://www.sthda.com/upload/boxplot_format.txt")
head(data2)
data1<-read.delim("https://www.w3.org/TR/PNG/iso_8859-1.txt")
head(data1)
data4 <- read.delim("https://github.com/mkuthan/example-spark/blob/master/src/main/resources/data/employees.txt")
head(data4)
library(readxl)
ir211wk12sample<- read_excel("D:/Sonali/data analytics/ir211wk12sample.xls")
View(ir211wk12sample)



install.packages("XML")
library("XML")
library("methods")

data5 <- xmlParse(file = "sample.xml")
print(data5)