
#pro fluxes,rho,momz,energ, mflz,momflzz, energflz

# ----------------------------------------------------------------------
#
# ROUTINE FLUXES
#
#    PURPOSE: Calculate the fluxes f_m, f_c, f_e 
#
#    INPUT ARGUMENTS: the primitive variables density, momentum and total
#                     energy rho, momz, energ
#    COMMON BLOCKS: Note that some necessary input is passed via common
#                       blocks (like the grid parameters and array zz, etc)
#    OUTPUT:  the fluxes mflz, momflzz, energflz 
# ----------------------------------------------------------------------

from dens2vpt import *

def fluxes(rho,momz,energ):

    # Calculate vx, pres
    vz,pres=dens2vpt(rho,momz,energ)

    mflz = momz   # mass flux
    momflzz = momz*momz/rho+pres   # momentum flux
    energflz = (energ + pres) * vz   # energy flux

    return mflz,momflzz,energflz
