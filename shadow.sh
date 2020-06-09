#!/bin/sh
#PBS -q q200p48h@shadow.hpc.MsState.Edu
#PBS -N MgBWQ
#PBS -l nodes=1:ppn=20
#PBS -l walltime=48:00:00
#PBS -A 060803-362098
# email notification
#PBS -m bea
#PBS -r n
#PBS -V
cd $PBS_O_WORKDIR
ml intel
source /usr/local/intel-2018.1/impi/2018.1.163/bin64/mpivars.sh intel64
source /usr/local/intel-2018.1/mkl/bin/mklvars.sh intel64


for i in `seq P Q`;
do
mpirun -np 20 /home/doyl/qe-2/q-e-qe-6.4.1/bin/pw.x -in hcp_bulk_$i.in > hcp_bulk_$i.out
done
