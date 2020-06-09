#bash creatall.sh
# This file will be called by driver.sh
nmin=AA # starting file number !
nmax=AB # ending file number !
Final=AC # when to stop !
#natoms_change=AD # initial number of atoms change !
################## NO CHANGE #############################
nfiles=20 # how many files 15*20=300
# 15 lattice parameter, each LP has 20 angles and CA's
# 300 files for one temperature
tempRange=0.011 # initial temperature change (NO CHANGE)
mkdir inputs
while true
do
   for i in `seq ${nmin} ${nmax}`;
   do
      echo  "working on hcp_bulk_$i" 
      mkdir -p hcp_bulk_$i
      cp hcp_bulk.in perturb.py hcp_bulk_$i 
      cd hcp_bulk_$i
#      sed -i '' "s/XXX/${natoms_change}/g" perturb.py
      sed -i '' "s/YYY/${tempRange}/g" perturb.py
      python3.7 perturb.py hcp_bulk.in $i
      mv template.dat hcp_bulk_${i}.in
      sed -i '' "3s/S4/S${i}/g" hcp_bulk_${i}.in
      cp hcp_bulk_${i}.in ../inputs
      cd ..
   done
   nmin=$(($nmin+$nfiles))
   #echo $nmin
   nmax=$(($nmax+$nfiles))
   #echo $nmax
   #natoms_change=$(($natoms_change+1))
   tr=`expr $tempRange+0.002 | bc`
   tempRange=$tr
   if [ $nmin -eq $Final ];
   then
      echo "File No : $nmin"
      break
   fi
   sleep 1
done
rm -r hcp_bulk_*
