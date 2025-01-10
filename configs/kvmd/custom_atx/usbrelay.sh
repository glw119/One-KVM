#!/bin/bash

echo $USBRELAY
case $1 in
short)
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 1 on
	sleep 1
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 1 off
	;;
long)
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 1 on
	sleep 5
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 1 off
	;;
reset)
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 2 on
	sleep 1
	python3 /etc/kvmd/custom_atx/usbrelay.py $USBRELAY 2 off
	;;
*)
	echo "No thing."
	;;
esac
