"""
1 valid characters only

2 valid parenthesis rules:
    right parenthesis count == left parenthesis count   %
    calculate every cell : never start with a ) and never end with a ( %


3 operators
    2 operators are never in the vicinity  %
    number(,    )number ,       )( invalid : between two cells must be an operator  %%%

"""


validNumbers = "012345689"
mainOperators = "+-*/"

def ifIsANumber(p_character):
    if p_character != "":
         return (p_character in validNumbers)

    return 0

def calculateOperation(p_operator, p_number_1, p_number_2):
    p_number_1=float(p_number_1)
    p_number_2=float(p_number_2)
    if p_operator == "+": 
        return str((p_number_1) + (p_number_2))
    if p_operator == "-": 
        return str((p_number_1) - (p_number_2))
    if p_operator == "*": 
        return str((p_number_1) * (p_number_2))
    if p_operator == "/": 
        return str((p_number_1) / (p_number_2))

def is_operator(p_character):
    if p_character != "": 
        return (p_character in mainOperators)
    else: 
        return 0

def operatorPriority(p_character):
    if p_character in "+-": 
        return 0
    if p_character in "*/": 
        return 1
    

def CalculateProblem(p_string):
    p_string = list(p_string)
    rplist = []
    lplist = []
    num = ""  
    while len(p_string) > 0:
        c = p_string.pop(0)
        if len(p_string) > 0: d = p_string[0]
        else: d = ""
        if ifIsANumber(c):
            num += c
            if not ifIsANumber(d):
                lplist.append(num)
                num = ""
        elif is_operator(c):
            while True:
                if len(rplist) > 0: top = rplist[-1]
                else: top = ""
                if is_operator(top):
                    if not operatorPriority(c) > operatorPriority(top):
                        number2 = lplist.pop()
                        op = rplist.pop()
                        number1 = lplist.pop()
                        lplist.append(calculateOperation(op, number1, number2))
                    else:
                        rplist.append(c)
                        break
                else:
                    rplist.append(c)
                    break
        elif c == "(":
            rplist.append(c)
        elif c == ")":
            while len(rplist) > 0:
                c = rplist.pop()
                if c == "(":
                    break
                elif is_operator(c):
                    number2 = lplist.pop()
                    number1 = lplist.pop()
                    lplist.append(calculateOperation(c, number1, number2))

    while len(rplist) > 0:
        c = rplist.pop()
        if c == "(":
            break
        elif is_operator(c):
            number2 = lplist.pop()
            number1 = lplist.pop()
            lplist.append(calculateOperation(c, number1, number2))

    return lplist.pop()




validCharacters = "()+-/*0123456789"
Numbers = "0123456789"
Operators = "+-*/"
def isValidParenthesis(p_string):

    tempString = ""
    for i in p_string:
        if i in ["(",")"]:
            tempString+=i

    p_string = tempString
    lpc=0
    rpc=0
    for i in p_string:
        if i == "(" : lpc+=1
        if i == ")" : rpc+=1

    if lpc != rpc :
        print ("the number of left and right parenthesis dont match.")
        return 0

    maskString = p_string
    maskString1= ""
    loopRun = 1
    if  (len(p_string)==2) and (p_string[0]=="(") or (len(p_string)==0):
        return 1
    elif(len(p_string)==2) and (p_string[0]==")"):
        print("Invalid Parenthesis Structure!!")
        return 0

    while loopRun :
        for i in range(len(maskString)):
            if i != len(maskString)-1 :
                if (maskString[i]=="(") and (maskString[i+1]==")") :
                    maskString1 = list(maskString)
                    maskString1 [i] = " "
                    maskString1 [i+1] = " "
                    x = ""

                    for i in maskString1:
                        x+=i

                    maskString1=x
                    break

        maskString=""
        for i in maskString1 :
            if i != " ":
                maskString+=i

        # print(maskString)
        if (maskString[0]==")"):
            print("Invalid Parenthesis Structure!!")
            return 0
        if (len(maskString)==2):
            loopRun=0
        
            return 1


    return 1


def isValid(p_string):

    copyString = ""

    for i in p_string:
        if i not in [" ","\t"]:
            copyString+=i

    for i in copyString:
        if i not in validCharacters:
            print("Invalid character is used : ",i)
            return 0

    if not isValidParenthesis(p_string):
        return 0


    for i in range(len(p_string)):
        if i != len(p_string)-1:
            if ((p_string[i]==")") and (p_string[i+1]=="(")) or (
                (p_string[i] in Numbers) and (p_string[i+1]=="(")) or (
                (p_string[i]==")") and (p_string[i+1] in Numbers)):

                print("Missing Operator!")
                return 0

            if ((p_string[i] in Operators) and (p_string[i+1] in Operators)):
                print("Invalid use of Operators!")
                return 0
    return 1




def magic(p_string):

    if isValid(p_string):
        return CalculateProblem(p_string)
    else:
        print("Error")
        return "Failed"

    


