from src.server.calculate import calculate as calc


def start():

    print("Server is running.")


    # TESTING
    func_list = ["5*4", "5^4", "(5+6)", "(5*(4+ 3))", "4.0+5",
        "6//3.5", "run test"]    
    new_list = calc.calculate_list(func_list)

    print(new_list)