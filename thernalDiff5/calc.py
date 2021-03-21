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
    print("min val",np.amin(lol))
    index = np.where(lol == np.amin(lol))
    return index[0][0]

if __name__ == '__main__':
    data = read('thernalDiff5\phaseDiff.txt')
    phi = data / times * 2 * np.pi * -1
    print("phi is", phi)
    ratio = np.tan(phi) #tan(phi)
    print(ratio)

    a = np.linspace(0,3,100000)
    result = fnc.bei(a)/fnc.ber(a) #the bernoulli equations

    plt.plot(a,result)
    plt.ylim(-10, 10)
    index = []

    for i in range(len(ratio)):
        index.append(get_intersect(result,ratio,i)) #get interseciton


    x = a[index]
    print('x vals',x)
    #get x value

    plt.scatter(x,result[index]) #validate on plot
    a = np.linspace(0,10,100000)
    result = fnc.bei(a)/fnc.ber(a) #the bernoulli equations

    plt.plot(a,result)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Kelvin Equation illustrated')
    plt.legend(('tan(phi)', 'Kelvin Equation'))
    plt.show()

    #calculate m
    m = omega*(9.594/2/x)**2
    print(m)
    m_bar = np.mean(m)
    print('m vals',m_bar)

    # phase plot of 
    t = np.linspace(0, 10, 10000)
    plt.plot(t, np.angle(fnc.ber(t) + 1j * fnc.bei(t)))
    
    plt.xlabel('x')
    plt.ylabel('phi(x)')
    plt.title('Phase angle of J_0')
    plt.show()

    t = np.linspace(0, 10, 10000)
    plt.plot(t, fnc.ber(t))
    plt.plot(t, fnc.bei(t))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of ber(x) and bei(x) for Real Values of x')
    plt.legend(('ber(x)', 'bei(x)'))
    plt.show()
    '''
    err_domain = np.linspace(1, 1.3, 500)

    coeffs = np.polyfit(err_domain, fnc.bei(err_domain)/fnc.ber(err_domain), deg=2)
    print("coeffs: ", coeffs)
    
    def quadfit(x): return coeffs[0] * x ** 2 + coeffs[1] * x + coeffs[2]

    plt.plot(a, quadfit(a))
    
    L1_err = fnc.bei(err_domain)/fnc.ber(err_domain) - quadfit(err_domain)
    L1_err = np.abs(L1_err)
    L1_err_val = np.mean(L1_err)
    print("L1 error:", L1_err_val)
    plt.show()
    '''