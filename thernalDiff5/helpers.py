import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

# helper file for helpful functions

def reader(filename:str):
    f = open(filename,'r')
    lines = np.asarray(f.readlines())
    f.close()
    time = []
    temp = []
    for i in lines:
        t,T,stamp = i.split('\t')
        try:
            time.append(float(t))
            temp.append(float(T))
        except:
            continue
    return np.asarray(time), np.asarray(temp)

