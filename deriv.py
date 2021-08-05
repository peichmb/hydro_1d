# ----------------------------------------------------------------------
# FUNCTION DERIV 
#
#    PURPOSE:  Calculate the numerical derivative with respect to zz 
#              of the input variable at the midpoints through centered finite 
#              differences.  
#
#    INPUT ARGUMENTS:  - var: an array containing the input variable. It must
#                        have the same number of components as zz. 
#                      
#    COMMON BLOCKS: Note that npz and zz are passed through common blocks
#
#    OUTPUT:  an array of npz-1 components (one less than var) containing the 
#             numerical approximation to the derivative at the midpoints. 
# ----------------------------------------------------------------------


import grid_common as gr

def deriv(var):
        
        return (var[1:]-var[:-1])/(gr.zz[1:]-gr.zz[:-1])
