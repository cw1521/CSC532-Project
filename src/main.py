from server import *
from client import *
from clientserver import *
import sys




if __name__ == "__main__":

    args = sys.argv

    if args[1] == "s":
        server.start()
    elif args[1] == "c":
        client.start()
    elif args[1] == "cs":
        clientserver.start()