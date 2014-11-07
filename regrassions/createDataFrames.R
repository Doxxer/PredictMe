


createDataFrame <- function(data, person.id, Rating) {
  data$X.. <- NULL
  groups <- levels(factor(data[[1]]))
  person.id <- c()
  Rating <- c()
  for (cur.group in groups) {
    g <- subset(data, data[[1]] %in% cur.group)
    person.id <- c (person.id, cur.group)
    Rating <- c(Rating, mean(g$Rating))
  }
  df = data.frame(person.id, Rating)
  df
}

Person <- c()
Rating <- c()

#рейтинг режиссеров
data.directors <- read.csv("..//Data//DirectorFULL.csv")
data.directors.result <- createDataFrame(data.directors, Person, Rating)
write.csv(data.directors.result, "DirectorsRating.csv")

#рейтинг актеров
data.actors <- read.csv("..//Data//ActorsFULL.csv")
data.actors.result <- createDataFrame(data.actors, Person, Rating)
write.csv(data.actors.result, "ActorsRating.csv")

#рейтинг продюссеров
data.producers <- read.csv("..//Data//ProducerFULL.csv")
data.producers.result <- createDataFrame(data.producers, Person, Rating)
write.csv(data.producers.result, "ProducersRating.csv")

#рейтинг писателей
data.writers <- read.csv("..//Data//WriterFULL.csv")
data.writers.result <- createDataFrame(data.writers, Person, Rating)
write.csv(data.writers.result, "WritersRating.csv")

