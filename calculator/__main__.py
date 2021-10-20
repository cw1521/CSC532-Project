import sys


def start_port(app, port):
    if app == 's':
        from src.server import server
        server.start(port)
    elif app == 'c':
        from src.client import client
        client.start(port)
    elif app == 'cs':
        from src.clientserver import clientserver
        clientserver.start(port)


def start(app):
    if app == 's':
        from src.server import server
        server.start()
    elif app == 'c':
        from src.client import client
        client.start()
    elif app == 'cs':
        from src.clientserver import clientserver
        clientserver.start()


args = sys.argv
app = args[1]
if len(args) > 2:
    port = int(args[2])
    start_port(app, port)
else:
    start(app)