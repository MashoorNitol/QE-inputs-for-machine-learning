import numpy as np
import os
import sys
import random
natoms=54
file=sys.argv[1]
dr=0.001*float(sys.argv[2])
command = 'grep '+ " -i 'ATOMIC_POSITIONS' "+file + ' -B -1 >template.dat'
os.system(command)
command = 'grep '+ " -i 'ATOMIC_POSITIONS' "+file + ' -A -1 >temp.dat'
os.system(command)
x,y,z=np.genfromtxt('temp.dat',skip_header=1,unpack=True,max_rows=natoms,usecols=[1,2,3])
#os.system('rm  temp.dat')
ntype=np.genfromtxt('temp.dat', dtype='S5',skip_header=1,unpack=True,max_rows=natoms,usecols=0)
dmax=YYY
list(ntype)
ntype.tolist()
#id=np.random.choice(np.arange(natoms),replace=True)
#print 'Randomly position displaced at:', (id+1),'th atom '
#print
for id in range(natoms):
    x[id]+=dmax*(2*np.random.random(1)[0]-1.0)
    y[id]+=dmax*(2*np.random.random(1)[0]-1.0)
    z[id]+=dmax*(2*np.random.random(1)[0]-1.0)


command = 'grep '+ " -i 'ATOMIC_POSITIONS' "+file + ' -B -1 >template.dat'
os.system(command)
#n=XXX
#if n>len(ntype):
#    ntype=["Al" for i in ntype]
#else:
#    for i in range(n):
#           position=random.randrange(0,len(ntype))
#           while ntype[position]=="Al":
#                   position=random.randrange(0,len(ntype))
#           ntype[position]="Al"
#
#print(ntype)


with open("coord.dat", "w") as output_file:
   for i in range(len(x)) :
       output_file.write(str(ntype[i],'utf-8')+'  ')
       #output_file.write('Al'+'  ')
       output_file.write(str(x[i])+'  ')
       output_file.write(str(y[i])+'  ')
       output_file.write(str(z[i])+'  ')
       output_file.write("\n")

command='cat coord.dat>>template.dat'
os.system(command)
command='tail -n 0 '+ file + ' >>template.dat '
#command='tail -n 0 '+ file + ' >>template.dat '
os.system(command)
