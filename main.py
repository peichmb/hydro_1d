# coding=latin-1

# ---------------------------------------------------------
# THIS IS THE MAIN PROGRAM OF THE CODE. 
#   -> It constitutes the decision and task-distribution center. 
#   -> It carries out a limited number of assignments itself. 
# ---------------------------------------------------------


# Import modules containing common variables, parameters and routines

import numpy as np              # Mathematical package to perform IDL-style array operations
from routines import *          # Module containing references to all the routines called from __main__
import grid_common as gr        # Module containing the numerical mesh and related parameters        
import params_common as par     # Module containing problem parameters, such as equilibrium density, etc...
from sys import argv            # argv contains the name of the program and the command line arguments


# --------------------------------------
# READ PARAMETERS FROM INPUT FILE
# --------------------------------------

if len(argv)==1:            # No file specified...
    exit('Please, specify input file...')
else:
    filename=argv[1]        # The filename identifies the experiment being carried out throughout the program.
                            #   (See, for instance, exp_ctrl.py).
read_input(filename)

print
print 'Experiment '+filename+' on course...'
print 'Taking '+str(gr.nint)+' intervals between '+str(gr.z0)+' and '+str(gr.zf)+'.'

# After this call to read_input(), the following variables are
# available in the __main__ module's symbol table:
#   itmax               -> Maximum number of iterations
#   timefinal           -> Time at which simulation ends
#   plottimeinterv      -> ]
#   plotstinterv        -> ] Cadence for output


# --------------------------------------
# READ PARAMETERS FROM INPUT FILE -- END
# --------------------------------------


# -------------------------
#  INITIAL CONDITIONS 
# -------------------------

vz0,rho0,pres0=initcond()

momz0 = rho0*vz0 
energ0 = pres0/(par.gam-1.) + rho0*vz0*vz0/2. 

# -------------------------
#  INITIAL CONDITIONS - end
# -------------------------
 
# --------------------------------------------------
# INITIALIZE VARIABLES JUST BEFORE STARTING THE LOOP
# --------------------------------------------------

vz=np.copy(vz0)
rho=np.copy(rho0)
pres=np.copy(pres0)

momz=np.copy(momz0)
energ=np.copy(energ0)

rhon=np.copy(rho0)
momzn=np.copy(momz0)
energn=np.copy(energ0)

rhonn=np.copy(rho0)
momznn=np.copy(momz0)
energnn=np.copy(energ0)

it=0
time=0.
fstop=False

# --------------------------------------------------------
# INITIALIZE VARIABLES JUST BEFORE STARTING THE LOOP - end
# --------------------------------------------------------


# Plot initial conditions:
if plottimeinterv !=0:
    plotrout(rho0,pres0,vz0,time,it)
    raw_input('press enter...')

# ----------------------------
# BIG LOOP BEGINS
# ----------------------------

while it<itmax and time<timefinal and not fstop: # fstop === Force stop

#   CALCULATE FLUXES FROM DENSITIES
    mflz,momflzz,energflz=fluxes(rho,momz,energ)
        
#   TIMESTEP
    dt=cfl(rho,momz,pres)
    
#   UPDATE TO HALF TIMESTEP  
    rhon,momzn,energn=update(dt,rho,momz,energ,mflz,momflzz,energflz,'half')
    
#   CALCULATE FLUXES FROM DENSITIES IN NEW GRID POINTS
    mflz,momflzz,energflz=fluxes(rhon,momzn,energn)

#   UPDATE TO FULL TIMESTEP    
    rhonn,momznn,energnn=update(dt,rho,momz,energ,mflz,momflzz,energflz,'full') 

#   BOUNDARY CONDITIONS
    rhonn=bcs(rhonn,'periodic')
    momznn=bcs(momznn,'periodic')
    energnn=bcs(energnn,'periodic')

#   CALCULATE PRIMITIVE VARIABLES FROM THE DENSITIES
    vznn,presnn=dens2vpt(rhonn,momznn,energnn)

#   EXCHANGE NEW AND OLD VARIABLES
    rho=rhonn
    momz=momznn
    energ=energnn
    pres=presnn
    vz=vznn

#   UPDATE TIME AND NUMBER OF ITERATIONS
    it+=1
    time+=dt

#   STORE RESULTS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#   CHECK IF EXPERIMENT IS COMPLETE
    fstop=exp_ctrl(filename) 

#   PLOT RESULTS 
    if plottimeinterv != 0 and (it%plottimeinterv==0 or it==itmax or time>timefinal or fstop):
        plotrout(rho,pres,vz,time,it)       
        
# ---------------
# BIG LOOP - end
# ---------------

print('program finished.')
print('     it='+str(it))
print('   time='+str(time))
print
raw_input('press enter...')
print

