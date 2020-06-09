import os
S=PP
F=QQ
mp=RR
A=9.580777213543405
a=A*mp
dir_prefix='hcp_bulk_'
d=0
while S < F:
    for j in range(S,S+20):
        #print(j)
        dir=dir_prefix+str(j)
        cmd1='sed -i -e '+'"11s/9.580777213543405/'+str(a) +'/g" '+dir+'.in'
        cmd2='sed -i -e '+'"12s/9.580777213543405/'+str(a) +'/g" '+dir+'.in'
        os.system(cmd1)
        os.system(cmd2)
        
    S+=20        
