# This routine controls when the experiment being carried out must stop, and gives appropriate output.

import numpy as np

def exp_ctrl(filename):    
    
    stop=False
    
    
    # EXPERIMENT 1C -----
    # -------------------
    
    if filename == 'exp1c.dat':
        from __main__ import rho
        from params_common import rho00, amp
        
        # Fraction of amplitude lost by numerical diffusion: 
        maxrho=np.max((rho-rho00)/rho00)
        minrho=np.min((rho-rho00)/rho00)
        frac=np.abs((2.*amp-(maxrho-minrho))/2./amp)
        fraclim=0.03
        
        if frac > fraclim:
            stop=True
            print
            print 'Experiment 1c finished: '
            print '  Full initial perturbation amplitude: '+str(2.*amp)
            print '  Full final perturbation amplitude: '+str(maxrho-minrho)
            print '  Fraction of full amplitude lost by numerical diffusion: '+str(frac)
            print '  Tolerance: '+str(fraclim)
            print
                        
    # EXPERIMENT 1C -END-
    # -------------------
    
    return stop       
        
