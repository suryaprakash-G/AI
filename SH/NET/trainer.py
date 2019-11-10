
import numpy as np
import tflearn
import tensorflow as tf
import random
import fileinput
import json

def main():

    while True:
        print('function-name# ')
        x = input()
        sep = x.split(" ")
        print("type# ")
        t = input()
        print("property ")
        p = input()
        print("linked ")
        l = input()
        fo = open(x+".dat", "w")
main()
def model():
    with open('intents.json') as json_data:
        intents = json.load(json_data)
    words = []
    classes = []
    documents = []
    ignore_words = ['?']
    # loop through each sentence in our intents patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # tokenize each word in the sentence
            w = nltk.word_tokenize(pattern)
            # add to our words list
            words.extend(w)
            # add to documents in our corpus
            documents.append((w, intent['tag']))
            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    tf.reset_default_graph()
    # Build neural network
    net = tflearn.input_data(shape=[None, len(train_x[-1])])
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, len(train_y[-1]), activation='softmax')
    net = tflearn.regression(net)