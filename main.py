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
        result = snippets.magic(String)
        print("\t",String,"\t:\t ",result)

testList = [
    "10+3*4-3",
    "5+(2+1)",
    "(10+12)-(3+(2+(5*5)))"
]

def main():
    print("input exit or quit to exit or quit. XD \n") 
    print("testList Table:")
    for i in testList:
        result = snippets.magic(i)
        print("\t",i,"\t:\t ",result)

    print("\n")

    while shouldRun :
        loop()
        print("\n")
main()