import re


def getValidationRegex():
    white_list = '''acos|asin|atan|atan2|ceil|cos|cosh|
        degrees|exp|fabs|floor|fmod|frexp|hypot|ldexp|
        log|log10|modf|pow|radians|sin|sinh|sqrt|tan|tanh'''
    regexString = '[^' + white_list + '|0-9|+\-\*/\^\(\).//]'
    return re.compile(regexString)



def isValidInput(funcString):
    regex = getValidationRegex()
    match = regex.search(funcString)
    if match == None:
        return True
    else:
        return False



def calculate(funcString):
    if isValidInput(funcString):
        funcString = funcString.replace("^", "**")
        try:
            answer = eval(funcString)
            return answer
        except:
            return "error"
    else:
        return "error"



def calculateList(funcList):
    newList = []
    for i in range(len(funcList)):
        funcString = funcList[i]
        newList.append((funcString, calculate(funcString)))
    return newList