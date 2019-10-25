import numpy as np
import tflearn
import tensorflow as tf
import random
import json

while True:
    print('sh::')
    x = input()
    sep = x.split(" ")
    print(sep)

def model():
    tf.reset_default_graph()
    # Build neural network
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
    net = tflearn.regression(net)