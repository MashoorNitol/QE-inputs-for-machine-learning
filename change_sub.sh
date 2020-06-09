#!env bash
start=1
end=5
for counter in `seq 1 300`;
do
echo $start
echo $end
sed -i ''  "17s/P/$start/g; 17s/Q/$end/g" shadow_$counter.sh
#sed -i '' "19s/Q/$end/g" shadow_$counter.sh
sed -i ''  "3s/WQ/$end/g" shadow_$counter.sh
start=$(($start+5))
end=$(($end+5))
done
