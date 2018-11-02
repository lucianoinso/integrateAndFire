import matplotlib.pyplot as plt


# Equation
def integAndFireFun(t, v):
    return (vrest - v + iCurrent*rm)/(taum)


def t4(x, y, h):
    k1 = integAndFireFun(x, y)
    k2 = integAndFireFun(x + (h / 2.0), y + k1*(h/2.0))
    k3 = integAndFireFun(x + (h / 2.0), y + k2*(h/2.0))
    k4 = integAndFireFun(x + h, y + (k3*h))
    return ((1/6.0)*(k1 + 2*k2 + 2*k3 + k4))


def rungeKutta(v0, h, iter):
    t = t0
    v = v0

    result = [(t, v)]

    for i in range(0, iter):
        if (v == vpeak):
            v = vrest
        vn = v + (h * t4(t, v, h))
        t = t + h
        v = vn
        if(v >= vthresh):
            v = vpeak
        result.append((t, v))
    return result


def plotIntAndFire(t, v):
    # Use LaTeX
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', size='10')

    plt.grid()
    plt.plot(t, v, 'black')  # , label='Voltaje [mV]')#, linestyle='dotted')

    plt.axhline(y=vthresh, linewidth=1, color='black',
                linestyle='dashed', label='Umbral de disparo')
    plt.title('$I_{e} = ' + str(iCurrent) + 'nA$', fontsize='16')
    plt.xlabel("Tiempo - t [ms]", fontsize='12')
    plt.ylabel("Potencial de membrana - V [mV]", fontsize='12')
    axes = plt.gca()

    plt.yticks(range(-65, 45, 15))

    # X axis range
    # axes.set_xlim([0, 200])
    # Y axis range
    # axes.set_ylim([-65, max(v) + 1])
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Parameters
    taum = 10
    rm = 10
    vrest = -65
    vthresh = -50
    iCurrent = 2
    t0 = 0
    v0 = vrest
    vpeak = 40
    tfinal = 200
    deltaT = 0.1
    iters = (tfinal - t0) / deltaT

    result = rungeKutta(vrest, deltaT, int(iters))

    # Print in console the result in format:
    for i, j in result:
        print(str(i) + " - " + str(j))

    plotIntAndFire([i[0] for i in result], [j[1] for j in result])
