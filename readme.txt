Simple Load Balancer Read Me instructions:
1. Copy Controller.py and paths.file to pox folder of the pox installation.
2. Copy ping scripts and http traffic generation scripts and stat.py files to mininet VM's home directory.
3. Execute following series of commands: 
a) sudo killall controller
Also cleanup any previous topology
sudo mn -c
b) Change directory into pox installation folder
cd ./pox
./pox.py log.level --DEBUG controller openflow.discovery
c) Open a new terminal and run the following:
sudo mn --custom topo.py --topo mytopo --controller remote --switch ovsk
d) mininet> h1 python -m SimpleHTTPServer 80 &
e) mininet> h2 wget -O - h1
	mininet> h3 wget -O - h1
	mininet> h2 wget -O - h1
	mininet> h3 wget -O - h1
f) mininet> h2 python call_2.py
	mininet> h3 python call_3.py
	mininet> h1 python call_1.py
g) mininet> sh python stat.py
