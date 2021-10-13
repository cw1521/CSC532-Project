
import sys


def start(app):
    if app == "s":
        from src.server import server
        server.start()
    elif app == "c":
        from src.client import client
        client.start()
    elif app == "cs":
        from src.clientserver import clientserver
        clientserver.start()



    
args = sys.argv
app = args[1]

start(app)