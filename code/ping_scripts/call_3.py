# script for pinging the client 1 and 2 from 3
import urllib, os
os.system("ping -c 5 10.0.0.2 | tail -1| awk '{print $4}' | cut -d '/' -f 2 >> ping_stat_3_2")
os.system("ping -c 5 10.0.0.1 | tail -1| awk '{print $4}' | cut -d '/' -f 2 >> ping_stat_3_1")
