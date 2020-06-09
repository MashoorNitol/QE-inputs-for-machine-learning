m=1
n=21
f=301

for i in `seq 1 5`;do
   cp again.sh all$i.sh
   sed -i '' "1s/A1/${m}/g" all$i.sh
   sed -i '' "2s/A2/${n}/g" all$i.sh
   sed -i '' "3s/A3/${f}/g" all$i.sh
   bash all$i.sh
   m=$(($m+300))
   n=$(($n+300))
   f=$(($f+300))
done
rm all*
