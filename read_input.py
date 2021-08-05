# coding = latin-1

import __main__
import numpy as np
import grid_common as gr
import params_common as par
import plotrout

def leelinea(f):
    '''
    Reads a line from f, replaces the commas for spaces and splits it. 
    
    INPUT
    -----
    f: a file
    '''
    return f.readline().replace(',',' ').split()

def read_input(filename):
    
    f = open(filename,'r')

    # READ IN THE PARAMETERS FOR THE NUMERICAL MESH   
    gr.nint = int(leelinea(f)[0])
    linea = leelinea(f)
    gr.z0 = float(linea[0])
    gr.zf = float(linea[1])
    gr.dx = (gr.zf-gr.z0) / gr.nint
    gr.npz = gr.nint+2
    gr.zz = np.linspace(gr.z0 - gr.dx/2., gr.zf + gr.dx/2., gr.npz)
    
    f.readline() # Skip blank line

    # READ IN THE PARAMETERS FOR MAX ITERATIONS, TIME AND FOR OUTPUT PERIODICITY
    # Assign these values to __main__ module control variables

    __main__.itmax=int(leelinea(f)[0])
    __main__.timefinal=float(leelinea(f)[0])
    linea=leelinea(f)
    __main__.plottimeinterv=int(linea[0])
    __main__.plotstinterv=int(linea[1])

    f.readline() # Skip blank line
    
    # READ IN PLOTTING OPTIONS
    
    plotrout.drawpres=bool(int(leelinea(f)[0]))
    plotrout.drawrho=bool(int(leelinea(f)[0]))
    plotrout.drawvz=bool(int(leelinea(f)[0]))
    plotrout.drawdot=bool(int(leelinea(f)[0]))
    plotrout.drawwave=bool(int(leelinea(f)[0]))
    
    f.readline() # Skip blank line 

    # READ IN THE PARAMETERS OF THE INITIAL CONDITION

    par.inittype=f.readline()[0:25].strip()
    par.shape=f.readline()[0:25].strip()
    par.amp=float(leelinea(f)[0])
    par.p00=float(leelinea(f)[0])
    par.rho00=float(leelinea(f)[0])
    par.vz00=float(leelinea(f)[0])
    par.gam=float(leelinea(f)[0])    
    par.cs00=np.sqrt(par.gam*par.p00/par.rho00)

    f.readline() # Skip blank line

    # READ IN THE CFL PARAMETER

    par.fcfl=float(leelinea(f)[0])

    f.close()


