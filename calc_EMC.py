def getEMC(T, RH):
    '''
    Knowing the ambient temperature and the relative humidity, it is possible to 
    calculate the equilibrium moisture content of wood, according to Hailwood-Horrobin equation.
    Inputs:
        - T: ambient temperature in celsius
        - RH: ambient relative humidity in %
    Output:
        - EMC: equilibrium moisture content
    '''
    T= T*9/5 + 32
    h= RH/100
    W = 0.00415*T**2 + 0.452*T + 330
    K = -0.000000844*T**2 + 0.000463*T + 0.791
    K1 = -0.0000935*T**2 + 0.000775*T + 6.34
    K2 = -0.0000904*T**2 + 0.0284*T + 1.09
    return 1800/W*((K*h/(1-K*h))+(K1*K*h+2*K1*K2*K**2*h**2)/(1+(K1*K*h+K1*K2*K**2*h**2)))