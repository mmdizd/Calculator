import snippets

shouldRun = True

def Input(p_placeholder):
    while True :
        In = input(p_placeholder)
        if len(In) != 0:
            return In
    

def loop():
    global shouldRun
    String = Input("please input the problem: ")
    if String in ["exit","quit"]:
        shouldRun = False
    else :
        snippets.magic(String)  

testList = [
    "1+2",
    "10*3",
    "13/9",
    "4-3",
    "10+3*4-3",
    "5+(2+1)",
    "(10+12)-(3+(2+(5*5)))"
]

def main():
    print("input exit or quit to exit or quit. XD ")
    while shouldRun :
        loop()
    for i in testList:
        result = snippets.magic(i)
        print(i,"\t:\t ",result)

main()