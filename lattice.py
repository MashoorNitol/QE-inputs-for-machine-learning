import numpy as np
a=15.551620647413015*0.97
inc_a=(15.551620647413015*1.03-15.551620647413015*0.97)/20
c=np.cos(np.deg2rad(120.5))
inc_c=(np.cos(np.deg2rad(119.5)) - np.cos(np.deg2rad(120.5)))/20
b=np.cos(np.deg2rad(90.5))
inc_b=(np.cos(np.deg2rad(89.5)) - np.cos(np.deg2rad(90.5)))/20
import os
LL=LLL
KK=KKK
dir_prefix='hcp_bulk_'
d=0
for i in range(LL,KK,1):
    a_new=a+d*inc_a
    b_new=b+d*inc_b
    c_new=c+d*inc_c
    for j in range(i,i+1):
        dir=dir_prefix+str(j)
        cmd1='sed -i -e '+'"13s/15.551620647413015/'+str(a_new) +'/g" '+dir+'.in'
        cmd2='sed -i -e '+'"14s/-0.5/'+str(c_new) +'/g" '+dir+'.in'
        cmd3='sed -i -e '+'"15s/0.0/'+str(b_new) +'/g" '+dir+'.in'
        cmd4='sed -i -e '+'"16s/0.0/'+str(b_new) +'/g" '+dir+'.in'
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
        os.system(cmd4)
    d+=1
