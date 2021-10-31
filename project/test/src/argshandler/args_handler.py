def test_port(arg):
    args = arg.split('=')
    if len(args) == 2 and args[0].lower() == '-p':
        try:
            port = int(args[1])
            return True
        except:
            print('Port must be an integer.')
            return False
    elif len(args) == 2 and args[0].lower() == '-h':
        print(f'Initialization using the host -h argument requires a port -p argument.')
    else:
        print(f'Invaid argument: {arg}')
        return False




def get_default_host(arg):
    args_list = []
    args = arg.split('=')
    args_list.append('127.0.0.1')
    args_list.append(int(args[1]))
    return args_list



def test_host_port(args):
    arg1 = args[0].split('=')
    arg2 = args[1].split('=')
    if len(arg1) == 2 and len(arg2) == 2:
        if arg1[0].lower() == '-h':
            return test_port(args[1])                      
        elif arg2[0].lower() == '-h':
            return test_port(args[0])                  
        else:
            print('Missing host -h argument.')
            return False
    else:
        print(f'Print invalid arguments: {args}')
        return False



def get_host_port(args):
    args_list = []
    arg1 = args[0].split('=')
    arg2 = args[1].split('=')
    if arg1[0].lower() == '-h':
        if arg2[0].lower() == '-p':                    
            args_list.append(arg1[1])
            args_list.append(int(arg2[1]))                      
    elif arg2[0].lower() == '-h':
        if arg1[0].lower() == '-p':
            args_list.append(arg2[1])
            args_list.append(int(arg1[1]))      
    return args_list 



# args for server.py
def test_server_args(args):
    # just port passed in
    if len(args) == 1:
        return test_port(args[0])
    # host and port passed in
    elif len(args) == 2:
        return test_host_port(args)
    else:
        print('Invalid number of arguments. A server must be initialized using the -p argument or -h and -p arguments. If a host is not specified using the -h argument, the default host "127.0.0.1" will be used.')
        return False



# args for server.py
def get_server_args(args):
    if test_server_args(args):
        args_list = []
        # just port passed in
        if len(args) == 1:
            args_list = get_default_host(args[0])
        # host and port passed in
        elif len(args) == 2:
            args_list = get_host_port(args)                 
        return args_list
    else:
        quit()
        



def test_client_args(args):
    if len(args) == 0:
        return True
    else:
        if len(args) == 1:
            return test_port(args[0])
        if len(args) == 2:
            return test_host_port(args)
        else:
            print('Invalid number of arguments. A client must be initialized with no arguments, a port -p, or a host -h and a port -p. If values are not provided for a host or a port, the default host="127.0.0.1" and port=65000 will be used.')
            return False




def get_client_args(args):
    if test_client_args(args):
        args_list = []
        if len(args) == 0:
            args_list.append('127.0.0.1')
            args_list.append(65000)
        elif len(args) == 1:
            args_list = get_default_host(args[0])
        elif len(args) == 2:
            args_list = get_host_port(args)
        return args_list
    else:
        quit()

    

def is_server1_arg(arg):
    if '-sh1=' in arg.lower() or '-sp1=' in arg.lower():
        return True
    else:
        return False

def is_server2_arg(arg):
    if '-sh2=' in arg.lower() or '-sp2=' in arg.lower():
        return True
    else:
        return False


def is_host_port_arg(arg):
    if '-h=' in arg.lower() or '-p=' in arg.lower():
        return True
    else:
        return False



def test_host_port_args(hp_args_list):
    # print(hp_args_list)
    if len(hp_args_list) == 0:
        return True
    elif len(hp_args_list) == 1:
        return test_port(hp_args_list[0])
    elif len(hp_args_list) == 2:
        return test_host_port(hp_args_list)
    else:
        return False


def server_args_conversion(arg):
    arg = arg.lower()
    new_arg = arg.replace('sh1', 'h').replace('sh2', 'h')
    new_arg = arg.replace('sp1', 'p').replace('sp2', 'p')
    return new_arg



def test_cs_server_args(args):
    if len(args) == 1:
        arg = server_args_conversion(args[0])
        return test_port(arg)
    elif len(args) == 2:
        arg1 = server_args_conversion(args[0])
        arg2 = server_args_conversion(args[1])
        return test_host_port([arg1, arg2])
    else:
        return False



def test_client_server_args(args):
    hp_args_list = list(filter(is_host_port_arg, args))
    server1_args_list = list(filter(is_server1_arg, args))
    server2_args_list = list(filter(is_server2_arg, args))
    # print(server1_args_list)
    if test_host_port_args(hp_args_list):
        if test_cs_server_args(server1_args_list) and test_cs_server_args(server2_args_list):
            return True
        else:
            print('Client server must be initialized with a port for server1 -sp1 and a port for server2 -sp2. If a value for server1 host -sh1 or server2 host -sh2 are not provided, the default "127.0.0.1" will be used.')
            return False
    else:
        return False

def get_cs_server_args(args):
    args_list = []
    if len(args) == 1:
        arg = server_args_conversion(args[0])
        args_list = get_default_host(arg)
    elif len(args) == 2:
        arg1 = server_args_conversion(args[0])
        arg2 = server_args_conversion(args[1])
        args_list = get_host_port([arg1, arg2])

    return args_list


def get_client_server_args(args):
    if test_client_server_args(args):
        hp_args_list = list(filter(is_host_port_arg, args))
        server1_args_list = list(filter(is_server1_arg, args))
        server2_args_list = list(filter(is_server2_arg, args))

        if len(hp_args_list) == 0:
            hp_args = ['127.0.0.1', 65000]
        elif len(hp_args_list) == 1:
            hp_args = get_default_host(hp_args_list[0])
        else:
            hp_args = get_host_port(hp_args_list)
            
        server1_args = get_cs_server_args(server1_args_list)
        server2_args = get_cs_server_args(server2_args_list)

        args_list = [hp_args[0], hp_args[1], server1_args[0], server1_args[1], server2_args[0], server2_args[1]]
        return args_list
    else:
        quit()

