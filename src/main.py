from server import *
from client import *
from clientserver import *
import sys


# From command line type python main.py c to start client
# From command line type python main.py s to start server
# From command line type python main.py cs to start clientserver

if __name__ == "__main__":

    args = sys.argv

    if args[1] == "s":
        server.start()
    elif args[1] == "c":
        client.start()
    elif args[1] == "cs":
        clientserver.start()