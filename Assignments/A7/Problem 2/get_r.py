import numpy as np
def get_r(K, L, alpha, Z, delta):
    '''This function generates the interest rate or vector of interest rates'''
    if type(K) == type(L) and 0 < alpha < 1 and 0 < delta < 1 and Z > 0:
        if K > 0 and L > 0:
            r = alpha * Z * ( L / K ) ** ( 1 - alpha) - delta
            return r
        elif len(K) == len(L):
            r = np.zeros(len(K))
            for i in range(len(K)):
                if K[i] <= 0 or L[i] <=0:
                    return
                else:
                    r[i] = alpha * Z * ( L[i] / K[i] ) ** ( 1 - alpha) - delta
            return r  
        else:
            return
    else:
        return