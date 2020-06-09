m=1
n=21 # Number of ca and angles change in one lattice param
f=301
#nc=1
for i in `seq 1 5`;do
   cp CreateFile.sh all$i.sh
   sed -i '' "3s/AA/${m}/g" all$i.sh
   sed -i '' "4s/AB/${n}/g" all$i.sh
   sed -i '' "5s/AC/${f}/g" all$i.sh
 #  sed -i '' "6s/AD/${nc}/g" all$i.sh
   bash all$i.sh
   m=$(($m+300))
   n=$(($n+300))
   f=$(($f+300))
   #nc=$(($nc+1))
done
rm all*
cp lattice.py driver2.sh change.py again.sh inputs/
cd inputs
bash driver2.sh
mv lattice.py driver2.sh change.py again.sh ../
cd ..
python QE.py
