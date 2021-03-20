import helpers
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as fnc

times = np.array([300,240,180,120])*2
#print(times)

def read(filename):
    with open(filename,'r') as f:
        k = f.readline().split(',')
        for i in range(len(k)):
            k[i] = float(k[i])
        return np.array(k)

if __name__ == '__main__':
    data = read('thernalDiff5\phaseDiff.txt')
    ratio = np.tan(data/times)
    print(ratio)

    a = np.linspace(0,1.5,1000)

    #plt.plot(a,fnc.bei(a),a,fnc.ber(a))
    plt.plot(a,fnc.bei(a)/fnc.ber(a))
    #plt.plot(ratio)
    plt.show()
