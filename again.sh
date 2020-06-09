SS=A1
EE=A2
Final=A3
mp=0.97
while true
do
   echo $SS
   echo $EE
   echo $mp
   cp change.py temp_$SS.py
   cp lattice.py ca_$SS.py
   sed -i '' "2s/PP/$SS/g; 3s/QQ/$EE/g; 4s/RR/$mp/g" temp_$SS.py
   sed -i '' "s/LLL/$SS/g; s/KKK/$EE/g" ca_$SS.py
   python3.7 ca_$SS.py
   python3.7 temp_$SS.py
   SS=$(($SS+20))
   EE=$(($EE+20))
   mp=`expr $mp+0.0040000000000000036 | bc`
   if [ $SS -eq $Final ]; then
      break
   fi
   echo "Number: $SS"

   sleep 1
done
rm *.in-e temp_* ca_*
