library(MASS)
library(lattice)

data.movie <- read.csv("DataRegression.csv")
data.movie$Film <- NULL
data.movie$X <- NULL


model.linear.general <- lm(Rating ~ . - Producer, data = data.movie)
model.linear <- stepAIC(model.linear.general)
summary(model.linear)
model.linear

model.poly2.general <- lm(Rating ~ poly(Actor.Group1, Actor.Group2, Actor.Group3, Actor.Group4,Producer, Writer, Director, degree = 2), data = data.movie)
model.poly2 <- stepAIC(model.poly2.general)
summary(model.poly2)
model.poly2

rse <- function(r) sqrt(sum(r^2) / (length(r) - 2))
data.movie.train.i <- sample(nrow(data.movie), size=nrow(data.movie)*0.9)
data.movie.train <- data.movie[data.movie.train.i, ]
data.movie.test <- data.movie[-data.movie.train.i, ]

#model.poly2.train <- lm(Rating ~ poly(Actor.Group1, Actor.Group2, Actor.Group3, Actor.Group4, Writer, Director, degree = 2), data = data.movie.train)
#model.poly2.train <- stepAIC(model.poly2.train)
#summary(model.poly2.train)
#model.poly2.train
#data.movie.predicted <- predict(model.poly2.train, data.movie.test)
#c(rse(model.poly2.train$residuals), rse(data.movie.predicted - data.movie.test$Rating))

model.linear.general.train <- lm(Rating ~ . - Producer, data = data.movie.train)
model.linear.train <- stepAIC(model.linear.general.train)
summary(model.linear.train)
data.movie.linear.predicted <- predict(model.linear.train, data.movie.test)
c(rse(model.linear.train$residuals), rse(data.movie.linear.predicted - data.movie.test$Rating))
save(model.linear, file = "model.linear.rda")
summary(model.linear)

###################################

load("model.linear.rda")
data.movie.linear.predicted <- predict(model.linear, data.movie.test)
c(rse(model.linear$residuals), rse(data.movie.linear.predicted - data.movie.test$Rating))
