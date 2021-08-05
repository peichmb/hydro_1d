# ----------------------------------------------------------------------
# ROUTINE dens2vpt
#
#    PURPOSE:  Calculate the primitive variables vz and pres from the
#              densities of mass, momentum and energy
#
#    INPUT ARGUMENTS:  PLEASE, FILL THIS IN
#
#    COMMON BLOCKS: Note that some necessary input is passed via common
#                       blocks 
#
#    OUTPUT:  PLEASE, FILL THIS IN
# ----------------------------------------------------------------------

import params_common as par

def dens2vpt(rho,momz,energ):

    vz = momz/rho
    pres = (par.gam-1.)*(energ-momz*momz/2./rho)
    
    return vz,pres
