#!/bin/bash
# This script is called by webhook.py to manage an s6 service
# Example: ./s6-action.sh start transmission transmission-daemon

if [ $# -lt 3 ]
then
	echo "Usage : $0 action s6-dirname process-name"
	exit
fi

case "$1" in

kill)	echo "Sending SIGKILL signal to $3 in /var/runs6/services/$2"
	s6-svc -d /var/run/s6/services/$2
	pkill -9 $3
	;;
start)	echo "Starting $3"
	s6-svc -u /var/run/s6/services/$2
	;;

esac
