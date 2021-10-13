from server import *
from client import *
from clientserver import *
import sys


# From command line type python main.py c to start client
# From command line type python main.py s to start server
# From command line type python main.py cs to start clientserver
def main(app):
    if app == "s":
        server.start()
    elif app == "c":
        client.start()
    elif app == "cs":
        clientserver.start()


if __name__ == "__main__":

    args = sys.argv
    app = args[1]

    main(app)