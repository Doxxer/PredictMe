from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import os
import pickle


def trainNetwork(dataset, dim):
    net = buildNetwork(dim, dim, 1)
    trainer = BackpropTrainer(net, dataset)
    trainer.trainEpochs(4)
    return net


def getRating(actors, writers, directors):
    return (524181,), 1


def computeMovieRating(movie_year, actors, writers, directors):
    features, actor_dim = getRating(actors, writers, directors)
    if os.path.isfile('neuronet_' + actor_dim + '.data'):
        with open('neuronet_' + actor_dim + '.data', 'r') as f:
            net = pickle.load(f)
        movie_rating = net.activate((movie_year,) + features)
    elif os.path.isfile('dataset_' + actor_dim + '.data'):
        with open('dataset_' + actor_dim + '.data', 'r') as f:
            dataset = pickle.load(f)
        net = trainNetwork(dataset, actor_dim)
        with open('neuronet_' + actor_dim + '.data', 'wb') as f:
            pickle.dump(net, f)
        movie_rating = net.activate((movie_year,) + features)
    else:
        print "Dataset for dimendion " + actor_dim + " doesn't exist."
        raise
    return movie_rating