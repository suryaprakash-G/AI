
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
#def if __name__ == '__main__':
while true:
    print('chat# ')
    x = input()
    sep = x.split(" ")
    print("type# ")

def model():
    tf.reset_default_graph()
    # Build neural network
    net = tflearn.input_data(shape=[None, len(train_x[-1])])
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, len(train_y[-1]), activation='softmax')
    net = tflearn.regression(net)