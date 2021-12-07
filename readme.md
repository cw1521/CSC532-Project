# Distributed Calculator
CSC 532 Project
## Starting the Calculator
* Type _python calculator c arg-list_ to start the client from the command line

  * -h='client-server-ip' -p='client-server-port'

* Type _python calculator s arg-list_ to start the server from the command line

  * -p='server-port'

* Type _python calculator cs arg-list_ to start the clientserver from the command line

  * -h='client-server-ip' -p='client-server-port' -sh1='server1-host'  -sh2='server2-host' -sp1='server1-port' -sp2='server2-port'

### Example Initialization
Ip addresses need to be enclosed in quotes. Ports do not need to be enclosed in quotes.
Code assumes that there are two servers
* Local Initialization
  * Servers \
_python3 csc532-project/calculator s -p=64000_ \
_python3 csc532-project/calculator s -p=64001_ 
  * Client-Server \
_python3 csc532-project/calculator cs -p=65000 -sp1=64001 -sp2=64000_ 
  * Client \
_python3 csc532-project/calculator c_ 
* Initialization over a Network 
  * Servers \
_python3 csc532-project/calculator s -p=64000_ \
_python3 csc532-project/calculator s -p=64001_ 
  * Client-Server \
_python3 csc532-project/calculator cs -p=65000 -sh1='10.0.2.15' -sp1=64000 -sh2='10.0.2.4' -sp2=64001_ 
  * Client \
python3 csc532-project/calculator c -h='10.0.2.6' -p=65000_ 
