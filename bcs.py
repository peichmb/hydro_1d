#; ----------------------------------------------------------------------
#; ROUTINE BCS
#;
#;    PURPOSE:  Calculate the boundary conditions of a variable
#;    INPUT ARGUMENTS:  PLEASE, FILL THIS IN
#;
#;    COMMON BLOCKS: Note that some necessary input is passed via common
#;                       blocks (like the grid parameters and array zz, etc)
#;
#;    OUTPUT:  PLEASE, FILL THIS IN
#; ----------------------------------------------------------------------



def bcs(var,kind):
    
    if kind != 'periodic':
        exit('routine bcs: bc type not included')

# the if-clause for type is introduced for possible future extensions

    if kind == 'periodic':
        var[-1]=var[1]
        var[0]=var[-2]
        
    return var

