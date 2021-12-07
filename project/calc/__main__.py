from src.argshandler import args_handler as ah
import sys



def start(app, args):
    if app == 's':
        args = ah.get_server_args(args)
        from src.server import server
        server.start(args[0], args[1])
    elif app == 'c':
        args = ah.get_client_args(args)
        from src.client import client
        client.start(args[0], args[1])
    elif app == 'cs':
        args = ah.get_client_server_args(args)
        from src.clientserver import clientserver
        clientserver.start(args[0], args[1], args[2], args[3], args[4], args[5])



args = sys.argv
if len(args) > 1:
    app = args[1]
    args = args[2:]

    start(app, args)
else:
    print(f'Invalid arguments. The type of application must be passed as an argument')

