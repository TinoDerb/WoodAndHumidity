def calcAbsHumidity(T, RH, method):
    '''
    Inputs:
    - T: please give T in Kelvin (Tkelvin = Tcelsius + 273.15)
    - RH: relative humidity in %
    - method:
        - "ABS": returns the absolute humidity in g/m³
        - "VOL": returns the absolute humidity in g/kg
    Reference: https://reboil.com/res/2021/txt/20211002T0631Z_article..humidity_conversion_article_draft.pdf
    Paper author: Steven Baltakatei Sandoval
    '''
    P = 101300
    epsilon = 0.62198 
    t = T - 273.15
    P_hpa = P / 100
    ln_e_w = -6096*T**-1 + 21.2409642 - 2.711193*10**-2*T + 1.673952*10**-5*T**2 + 2.433502*np.log(T)
    e_w = np.exp(ln_e_w)
    e_w_hpa = e_w / 100
    f_w = 1 + (10**-4*e_w_hpa)/(273 + t)*(((38 + 173*np.exp(-t/43))*(1 - (e_w_hpa / P_hpa))) +\
                                          ((6.39 + 4.28*np.exp(-t / 107))*((P_hpa / e_w_hpa) - 1)))
    e_prime_w = f_w * e_w
    e_prime = (RH / 100) * e_prime_w
    if "ABS" in method:
        AH = (epsilon * e_prime) / (P - e_prime);
    elif "VOL" in method:
        R_v = 461.525
        c_1 = 10**5
        z = 1 - (70 - t)*P_hpa*10**-8
        d_v = (c_1 * e_prime/ 100) / (z * R_v * T)
        AH = d_v / 1000
    else:
        AH = np.nan
    return round(AH,5)*1000