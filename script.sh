
max=10
for i in `seq 2 $max`
do
    killall -9 chrome
    sleep 10
done