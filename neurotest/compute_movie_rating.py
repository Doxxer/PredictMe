from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import os
import pickle


def trainNetwork(dataset, dim):
    net = buildNetwork(3 + dim, 3 + dim, 1)
    trainer = BackpropTrainer(net, dataset)
    trainer.trainEpochs(4)
    return net


def getRating(actors, writers, directors):
    return (6.7, 5.7, 8.6), 1


def computeMovieRating(movie_year, actors, writers, directors):
    features, actor_dim = getRating(actors, writers, directors)
    if os.path.isfile('neuronet_' + str(actor_dim) + '.data'):
        with open('neuronet_' + str(actor_dim) + '.data', 'r') as f:
            net = pickle.load(f)
        movie_rating = net.activate((movie_year,) + features)
    elif os.path.isfile('dataset_' + str(actor_dim) + '.data'):
        with open('dataset_' + str(actor_dim) + '.data', 'r') as f:
            dataset = pickle.load(f)
        net = trainNetwork(dataset, actor_dim)
        with open('neuronet_' + str(actor_dim) + '.data', 'wb') as f:
            pickle.dump(net, f)
        movie_rating = net.activate((movie_year,) + features)
    else:
        print "Dataset for dimendion " + str(actor_dim) + " doesn't exist."
        raise
    return movie_rating

print computeMovieRating(0, 0, 0, 0)