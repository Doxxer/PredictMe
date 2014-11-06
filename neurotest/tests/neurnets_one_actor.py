#!/usr/bin/env python2

import pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


with open('datasets.pickle', 'r') as f:
    datasets = pickle.load(f)

print """All dataset is a random 100-samples.

Format:
ds=dataset_index, n=num_hidden_neurons, 1st_train_error, 2nd_train_error, 3rd_train_error, 4th_train_error
Errors for control set"""

ds = []

for idx, dataset in enumerate(datasets):
    ds.append([])
    ds[idx] = SupervisedDataSet(4, 1)
    for sample in dataset:
        ds[idx].addSample(sample[0], sample[1])

for d in range(4):
    for n in [1, 2, 3, 4]:
        net = buildNetwork(4, n, 1)
        trainer = BackpropTrainer(net, ds[0])
        print "ds={0}".format(d), "n={0}".format(n), trainer.train(), trainer.train(), trainer.train(), trainer.train()
        print "Control errors:"
        for sample in ds[5]:
            print abs(net.activate(sample[0])-sample[1])
#print trainer.trainUntilConvergence()
