
max=10000
for i in `seq 2 $max`
do
    killall -9 chrome
    sleep 20
done