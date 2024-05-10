from ase.build import surface
from ase.io import read,write
from ase.visualize import view
import sys

s=read('NiTe2-cod1.cif')
slab = surface(lattice=s, indices=[0,1,1],layers = 3 )

# write the output in a Espresso input with default parameters as saved in ase
slab.write('slab_011.pwi')  
view(slab)

