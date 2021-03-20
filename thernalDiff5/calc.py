import numpy as np
import matplotlib.pyplot as plt
import scipy.special as fnc

times = np.array([300,240,180,120])*2 #periods
omega = 2*np.pi/times #angular velocities 
print("omega", omega)

def read(filename):
    #read the data we have stored and convert to a numpy array
    with open(filename,'r') as f:
        k = f.readline().split(',')
        for i in range(len(k)):
            k[i] = float(k[i])
        return np.array(k)

def get_intersect(result,exp,i):
    #get interseciton of our values to the graph
    lol = abs(exp[i]-result)
    #print(np.amin(five_min))
    index = np.where(lol == np.amin(lol))
    return index[0][0]

if __name__ == '__main__':
    data = read('thernalDiff5\phaseDiff.txt')
    ratio = np.tan(data/times) #tan(phi)
    #print(ratio)

    a = np.linspace(0,1.5,1001)
    result = fnc.bei(a)/fnc.ber(a) #the bernoulli equations

    plt.plot(a,result)
    
    index = []

    for i in range(len(ratio)):
        index.append(get_intersect(result,ratio,i)) #get interseciton


    x = a[index]
    print('x vals',x)
    #get x value

    plt.scatter(x,result[index]) #validate on plot
    plt.show()

    #calculate m
    m = omega*(9.594/2/x)**2
    print(m)
    m_bar = np.mean(m)
    print('m vals',m_bar)
    