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

def square_wave(start_cold, start_hot, period, start:bool, domain_endtime:int):
    time = np.arange(domain_endtime+1)
    sqr = np.arange(domain_endtime+1)
    diff = start_hot - start_cold
    count = 0
    for i in range(len(sqr)):
        if count == period:
            count = 0
            if start == 1:
                start = 0
            else:
                start = 1
        sqr[i] = start_cold + start * diff
        count += 1
    return time, sqr
        
def get_dist(coord_dict):
    x_list = coord_dict['x']
    phase = []
    for i in range(0,len(x_list),2):
        phase.append(x_list[i+1]-x_list[i])
    return phase