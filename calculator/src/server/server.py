from src.server.calculate import calculate as calc


def start():

    print("Server is running.")


    # TESTING

    funcList = ["5*4", "5^4", "(5+6)", "(5*(4+ 3))", "run test"]    
    newList = calc.calculateList(funcList)

    print(newList)