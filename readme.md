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
_python calculator cs -p=65000 -sh1='127.0.0.1' -sp1=64000 -sh2='127.0.0.1' -sp2=64001_
* Ip addresses need to be enclosed in quotes. Ports do not need to be enclosed in quotes.
* Code assumes that there are two servers