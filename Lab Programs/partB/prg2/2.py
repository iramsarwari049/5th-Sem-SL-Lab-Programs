def ctof(c):
    return (c*(9/5) + 32)

def ftoc(p):
    return ((p-32)*(5/9))

def ctok(x):
    return (x+273.15)

def ktoc(y):
    return (y-273.15)

def ftok(a):
    return ctok(ftoc(a))

def ktof(b):
    return ctof(ktoc(b))

s = "y"
op1=[]
op2=[]
op3=[]
op4=[]
op5=[]
op6=[]


while(s=="y" or s == "Y"):
    op = input("Enter the selection: 1.C->F  2.F->C  3.C->K  4.K->C  5.F->K  6.K->F \n")
    if(op=="1" or op=="2" or op=="3" or op=="4" or op=="5" or op=="6"):
        if(op=="1"):
            c = float(input("Enter the temperature in celsius:  "))
            op1 = op1 +[(c,ctof(c))]
            print("Celsius to Farenhiet\n")
            print(sorted(op1))
        elif(op=="2"):
            p = float(input("Enter the temperature in farenhiet:  "))
            op2=op2 + [(p,ftoc(p))]
            print("Farenhiet to Celsius\n")
            print(sorted(op2))
        elif(op=="3"):
            x = float(input("Enter the temperature in celsius:  "))
            op3=op3 + [(x,ctok(x))]
            print("Celsius to Kelvin\n")
            print(sorted(op3))
        elif(op=="4"):
            y = float(input("Enter the temperature in kelvin:  "))
            op4 = op4+[(y,ktoc(y))]
            print("Kelvin to Celsius\n")
            print(sorted(op4))
        elif(op=="5"):
            a = float(input("Enter the temperature in farenhiet:  "))
            op5=op5+[(a,ftok(a))]
            print("Farenhiet to Kelvin\n")
            print(sorted(op5))
        elif(op=="6"):
            b = float(input("Enter the temperature in kelvin:  "))
            op6=op6+[(b,ktof(b))]
            print("Kelvin to Farenhiet\n")
            print(sorted(op6))
    else:
        print("Invalid Input")
    s = input("Enter Y to continue and N to terminate\n")
