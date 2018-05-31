#!/bin/bash
cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0/100))
cpuTempM=$(($cpuTemp2 % $cpuTemp1))
cpuTemp="$cpuTemp1.$cpuTempM"
gpuTemp=$(/opt/vc/bin/vcgencmd measure_temp)
gpuTemp2=${gpuTemp: 5:-2}

python /home/jeroen/TempLoggingSQL/DecConvSQL.py $cpuTemp $gpuTemp2 
 
