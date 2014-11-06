#!/usr/bin/env python2

import pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import numpy

with open('datasets.pickle', 'r') as f:
    datasets = pickle.load(f)

print """All datasets is a random 100-samples.

Format:
ds=dataset_index, n=num_hidden_neurons, 1st_train_error, 2nd_train_error, 3rd_train_error, 4th_train_error
Errors for control set"""

ds = []
feature_dim = 4

for idx, dataset in enumerate(datasets):
    ds.append([])
    ds[idx] = SupervisedDataSet(feature_dim, 1)
    for sample in dataset:
        #print sample[0], sample[1]
        ds[idx].addSample(sample[0], sample[1])

for d in range(4):
    for n in range(1, feature_dim+1):
        net = buildNetwork(feature_dim, n, 1)
        trainer = BackpropTrainer(net, ds[0])
        print "ds={0}".format(d), "n={0}".format(n), trainer.train(), trainer.train(), trainer.train(), trainer.train()
        print "Control set errors characteristics:"
        errs = numpy.zeros(len(ds[5]))
        for idx, sample in enumerate(ds[5]):
            errs[idx] = net.activate(sample[0])-sample[1]
        print "  min(abs) =", numpy.min(numpy.abs(errs))
        print "  0.05 percentile =", numpy.percentile(errs, 5)
        print "  mean =", numpy.mean(errs)
        print "  median =", numpy.median(errs)
        print "  std =", numpy.std(errs)
        print "  0.95 percentile =", numpy.percentile(errs, 95)
        print "  max(abs) =", numpy.max(numpy.abs(errs))
        #    print (net.activate(sample[0])-sample[1])
        #with open(str(d) + '_' + str(n) + '.outdata', 'w') as f:
        #    f.write(net.activateOnDataset(ds[5]))
        #print net.activateOnDataset(ds[5])
#print trainer.trainUntilConvergence()
