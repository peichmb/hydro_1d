# coding=latin-1

# ----------------------------------------------------------------------
# ROUTINE INITCOND
#
#    PURPOSE:  Calculate the arrays of density, velocity and pressure 
#                 at time t=0. 
#    INPUT ARGUMENTS: 
#              condition:   char variable with the choice of initial condition
#                 shape :   char variable with some subsidiary choice
#    COMMON BLOCKS: Note that some necessary input is passed via common
#                       blocks (like the grid parameters and array zz, etc)
#    OUTPUT:  the arrays rho0, vz0, pres0
# ----------------------------------------------------------------------

import numpy as np
import grid_common as gr
import params_common as par

def initcond():
    if par.inittype == 'sound wave':
        if par.shape == 'sine':      
            h = np.cos(2.*np.pi*((gr.zz-gr.z0)/(gr.zf-gr.z0)))
        if par.shape == 'test 1':
            h = np.sin(gr.zz+6.)**4. / (1.+np.cosh( (3.*(gr.zz+10.5))**2. ))         
        rho0 = par.rho00*(1.+par.amp*h)
        vz0= par.vz00+par.cs00*par.amp*h
        pres0= par.p00*(1.+par.gam*par.amp*h)
    if par.shape == 'other':
        exit('routine initcond: no other condition is implemented yet')

    return vz0,rho0,pres0
