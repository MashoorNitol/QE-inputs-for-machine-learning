import sys
#from importlib import reload
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
import os
import numpy as np
from numpy import linalg as LA
from array import *
import math
def get_all_coord(filename):
    """@returns all_coords
    """
    natoms=54
    a=np.genfromtxt(filename,skip_header=10,unpack=True,max_rows=1,usecols=2)
    b=np.genfromtxt(filename,skip_header=11,unpack=True,max_rows=1,usecols=2)
    c=np.genfromtxt(filename,skip_header=12,unpack=True,max_rows=1,usecols=2)
    cosab=np.genfromtxt(filename,skip_header=13,unpack=True,max_rows=1,usecols=2) # gamma
    gamma=math.degrees(math.acos(cosab))
    cosac=np.genfromtxt(filename,skip_header=14,unpack=True,max_rows=1,usecols=2) # beta
    beta=math.degrees(math.acos(cosac))
    cosbc=np.genfromtxt(filename,skip_header=15,unpack=True,max_rows=1,usecols=2) # alpha
    alpha=math.degrees(math.acos(cosbc))
    x,y,z=np.genfromtxt(filename,skip_header=37,unpack=True,max_rows=natoms,usecols=[1,2,3])
    ntype=np.genfromtxt(filename, dtype='S5',skip_header=37,unpack=True,max_rows=natoms,usecols=0)
    list(ntype)
    ntype.tolist()
    v1=np.array([a,0,0])
    v2=np.array([b*math.cos(math.radians(gamma)), b*math.sin(math.radians(gamma)), 0])
    v3=np.array([c*math.cos(math.radians(beta)),  c*(math.cos(math.radians(alpha))-math.cos(math.radians(beta))*math.cos(math.radians(gamma)))/math.sin(math.radians(gamma)), c*np.sqrt( 1 + 2*math.cos(math.radians(alpha))*math.cos(math.radians(beta))*math.cos(math.radians(gamma))- math.pow(math.cos(math.radians(alpha)),2)-math.pow(math.cos(math.radians(beta)),2) - math.pow(math.cos(math.radians(gamma)),2))/math.sin(math.radians(gamma))])

    V=np.vstack((v1, v2, v3))
    C=np.vstack((x,y,z))
    coord=np.matmul(np.transpose(C),V)

#print(coord)
    with open("Zinc54HCP.xyz", "a") as output_file:
        output_file.write(str(natoms))
        output_file.write("\n")
        output_file.write('Lattice="'+' '+str(v1[0])+' '+str(v1[1])+' '+str(v1[2])+' '+str(v2[0])+' '+str(v2[1])+' '+str(v2[2])+' '+str(v3[0])+' '+str(v3[1])+' '+str(v3[2])+' '+'" '+'Properties=species:S:1:pos:R:3')
        output_file.write("\n")
        for i in range(len(x)) :
            output_file.write(str(ntype[i])+'  ') 
            output_file.write(str(coord[i,0])+'  ')
            output_file.write(str(coord[i,1])+'  ')
            output_file.write(str(coord[i,2])+'  ')
            output_file.write("\n")
        return C 

if __name__=="__main__":
# directory name where the data files are located
    dir_name="/inputs/"
    input_dir="{0}{1}".format(os.getcwd(),dir_name )
    input_data=[f for f in os.listdir(input_dir) if ((os.path.isfile(os.path.join(input_dir,f))) and (os.stat(os.path.join(input_dir,f)).st_size > 0))]
    output=[]
    for fname in input_data:
        #print fname
        data="{0}{1}".format(input_dir,fname)
        output.extend(get_all_coord(data))       
