"""
1 valid characters only

2 valid parenthesis rules:
    right parenthesis count == left parenthesis count   %
    calculate every cell : never start with a ) and never end with a ( %


3 operators
    2 operators are never in the vicinity  %
    number(,    )number ,       )( invalid : between two cells must be an operator  %%%

"""




import pstats
from unittest import result


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


def calculateOperation(p_string):
    0

def calculateCell(p_string):
    result = 0



    return result
    

def calculateProblem(p_string):
    
    tempString = ""
    rpi = 0
    lpi = 0
    tempString1 = ""
    for i in range(len(p_string)):
        if i != len(p_string)-1:
            
            if (p_string[i] not in ["(",")"]):
                tempString+=p_string[i]
            elif (p_string[i]=="("):
                tempString=""
                rpi = i
            elif (p_string[i]==")") and (tempString!=""):
                lpi = i

                tempString1=""
                for c in range(len(p_string)):
                    if not ((c>=rpi) and (c<=lpi)):
                        tempString1+=p_string[c]

                print("\t",tempString1)
                print("\t",tempString)
                tempString=""
            
            
            

        else:


            if (p_string[i]!=")"): tempString+=p_string[i]
            if (tempString!="")  : 
                print("\t",tempString)


    return 0


def magic(p_string):
    myStack = []
    if isValid(p_string):
        return calculateProblem(p_string)
    else:
        print("Error")
        return "Failed"

    



