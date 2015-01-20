
GROUP.COUNT <- 4

changeColNames <- function(data) {
  colnames(data) <- c("Person", "Rating")
  data
}

normalizeFilmData <- function(data) {
  colnames(data) <- c("X..","Film", "Name", "Year", "Rating", "Budget", "Gener", "Votes")
  data$X.. <- NULL
  data$Gener <- NULL
  data$Votes <- NULL
  data
}

hasNA <- function(vector.data) {
  for (data in vector.data) {
    if (is.na(data)) {
      return(TRUE)
    }
    
  }
  return(FALSE)
}

getDataFromYear <- function(data, year1, year2) {
  data$X.. <- NULL
  data$Budget <- NULL
  result <- subset(data, Year > year1 & Year <= year2)
  result
}

getNumberGroup <- function(rating, group.count) {
  cur.step <- 0
  for (i in 1:group.count) {
    cur.step <- cur.step + 10.0 / group.count
    if (rating <= cur.step)
      return(i)
  }
}

groupRating <- function(data, rating.data, group.count) {
  result <- c(rep(0,group.count))
  for (cur.person in data) {
    cur.rating <- subset(rating.data, Person == cur.person)$Rating
    cur.num.group <- getNumberGroup(cur.rating, group.count)
    result[cur.num.group] <- result[cur.num.group] + 1
  }
  return(result)
}

meanRating <- function(data, rating.data) {
  rating.v <- c()
  for (cur.person in data) {
    cur.rating <- subset(rating.data, Person == cur.person)$Rating
    rating.v <- c(rating.v, cur.rating)
  }
  return(mean(rating.v))
}

rating.actors <- read.csv("..//repo/PredictMe//Data//CSV//ratedActors.csv")
rating.directors <- read.csv("..//repo/PredictMe//Data//CSV//ratedDirectors.csv")
rating.producers <- read.csv("..//repo/PredictMe//Data//CSV//ratedProducers.csv")
rating.writers <- read.csv("..//repo/PredictMe//Data//CSV//ratedWriters.csv")

rating.actors <- changeColNames(rating.actors)
rating.directors <- changeColNames(rating.directors)
rating.producers <- changeColNames(rating.producers)
rating.writers <- changeColNames(rating.writers)



data.movies <- read.csv("..//repo/PredictMe//Data//allMoviesSHORT.csv")
data.movies <- normalizeFilmData(data.movies)

data.directors <- read.csv("..//repo/PredictMe//Data//DirectorFULL.csv")
data.actors <- read.csv("..//repo/PredictMe//Data//ActorsFULL.csv")
data.writers <- read.csv("..//repo/PredictMe//Data//WriterFULL.csv")
data.producers <- read.csv("..//repo/PredictMe//Data//ProducerFULL.csv")

data.movies <- getDataFromYear(data.movies, "1990", "2014")
data.directors <- getDataFromYear(data.directors, "1990", "2014")
data.actors <- getDataFromYear(data.actors, "1990", "2014")
data.writers <- getDataFromYear(data.writers, "1990", "2014")
data.producers <- getDataFromYear(data.producers, "1990", "2014")

groups.films <- data.movies$Film 
  
Actor.Group1 <- c()
Actor.Group2 <- c()
Actor.Group3 <- c()
Actor.Group4 <- c()
Director <- c()
Writer <- c()
Producer <- c()
Film <- c()
Rating <- c()

step <- 0
for (cur.film in groups.films) {
  cur.data.v <- c()
  
  actors.group <- subset(data.actors, data.actors$Film %in% cur.film)
  actor.group.rating <- groupRating(actors.group$Actor, rating.actors, GROUP.COUNT)

  cur.data.v <- c(cur.data.v, actor.group.rating[1])
  cur.data.v <- c(cur.data.v, actor.group.rating[2])
  cur.data.v <- c(cur.data.v, actor.group.rating[3])
  cur.data.v <- c(cur.data.v, actor.group.rating[4])
  
  directors.group <- subset(data.directors, data.directors$Film %in% cur.film)
  director.mean <- meanRating(directors.group$Director, rating.directors)
  cur.data.v <- c(cur.data.v, director.mean)
  
  cur.data.v <- c(cur.data.v, cur.film)
  cur.data.v <- c(cur.data.v, directors.group$Rating[1])
  
  writers.group <- subset(data.writers, data.writers$Film %in% cur.film)
  writers.mean <- meanRating(writers.group$Writer, rating.writers)
  cur.data.v <- c(cur.data.v, writers.mean)
   
  producers.group <- subset(data.producers, data.producers$Film %in% cur.film)  
  producer.mean <-meanRating(producers.group$Producer, rating.producers)
  cur.data.v <- c(cur.data.v, producer.mean)
  
  if (!hasNA(cur.data.v)) {
    Actor.Group1 <- c(Actor.Group1, actor.group.rating[1])
    Actor.Group2 <- c(Actor.Group2, actor.group.rating[2])
    Actor.Group3 <- c(Actor.Group3, actor.group.rating[3])
    Actor.Group4 <- c(Actor.Group4, actor.group.rating[4])
    Director <- c(Director, director.mean)
    Film <- c(Film, cur.film)
    Rating <- c(Rating, directors.group$Rating[1])
    Writer <- c(Writer, writers.mean)
    Producer <- c(Producer, producer.mean) 
  }
  step <- step + 1
  cat(step)
  cat(" ")
}

data.regression <- data.frame(Film, Rating, Actor.Group1, Actor.Group2, Actor.Group3, Actor.Group4, Director, Producer, Writer)
write.csv(data.regression, "DataRegression.csv")

