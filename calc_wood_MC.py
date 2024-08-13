def convertRToMC(R, T = np.nan):
    '''
    Inputs: resistance of the wood piece in Megaohm
    returns the MC of wood in %
    Reference: https://www.diva-portal.org/smash/get/diva2:1080039/FULLTEXT01.pdf
    Please consider adjusting the parameters of the curve for your specific wood species
    '''
    if np.isnan(T):
        MC = -np.log((np.log(R)+2.79)/26)/0.0845 # convert the wood resistance into moisture content
        return round(MC,2) # return two-decimal rounded results
    else:
        MC_C = (MC+0.567-0.026*(T+2.8)+0.000051*T**2)/(0.881*1.0056**(T+2.8)) # correct MC
        return round(MC_C,2)
