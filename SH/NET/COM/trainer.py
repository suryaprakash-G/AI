
import numpy as np
import random
import fileinput
import json

def main():
    fo = open("train" + ".dat", "w")
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
        fo.write("t-"+t+"\np-"+p+"\nl-"+l);
    fo.close();
main()
