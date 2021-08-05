# ----------------------------------------------------------------------
# ROUTINE UPDATE 
#
#    PURPOSE:  Calculate variables at timestep n+1/2 (half) or n+1 (full).
#
#    INPUT ARGUMENTS:  - the densities at timestep n, namely rho, momz, energ
#                      - the fluxes mflz, momflzz, energflz
#                      - the request of half or full timestep (/half, /full)
#
#    COMMON BLOCKS: Note that some necessary input is passed via common
#                       blocks (like the grid parameters and array zz, etc)
#
#    OUTPUT:  the densities at timestep n+1/2 (half) or at timestep n (full),
#                       namely rhon, momzn, energn
# ----------------------------------------------------------------------



from deriv import *
import grid_common as gr
import numpy as np



def update(dt,rho,momz,energ,mflz,momflzz,energflz,mode):

    # ----------------------
    # DERIVATIVES OF FLUXES 
    # ----------------------
    
    mflzcz = deriv(mflz)
    momflzzcz = deriv(momflzz)
    energflzcz = deriv(energflz)
    
    
    # -----------------------
    # UPDATE TO HALF TIMESTEP
    # -----------------------

    if mode=='half':
    
        rhomid = (rho[:-1] + rho[1:])/2.
        momzmid = (momz[:-1] + momz[1:])/2.
        energmid = (energ[:-1] + energ[1:])/2.
    
        rhon = rhomid - dt/2.*mflzcz
        momzn = momzmid - dt/2.*momflzzcz 
        energn = energmid - dt/2.*energflzcz

        rhon=np.append(rhon,1.)
        momzn=np.append(momzn,1.)
        energn=np.append(energn,1.)        
        
    # -----------------------
    # UPDATE TO FULL TIMESTEP
    # -----------------------

    elif mode=='full':
    
        rhon=np.empty(gr.npz,dtype=float)
        momzn=np.empty(gr.npz,dtype=float)
        energn=np.empty(gr.npz,dtype=float)
                
        rhon[1:-1]=rho[1:-1] - dt*mflzcz[:-1] # mirar esto...
        momzn[1:-1]=momz[1:-1] - dt*momflzzcz[:-1]
        energn[1:-1]=energ[1:-1] - dt*energflzcz[:-1]        
        
        
    return rhon,momzn,energn

