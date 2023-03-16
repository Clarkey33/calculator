#basic calculator functions defined

def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer)+"\n") #used concatenation to display answer
 
def sub(a,b):
    answer= a-b
    print(str(a) + "-" + str(b) + "=" + str(answer)+"\n") #used concatenation to display answer

def mul(a,b):
    answer= a*b
    print(str(a) + "*" + str(b) + "=" + str(answer)+"\n") #used concatenation to display answer
 
def div(a,b):
    if b == 0:
        print('cannot divide by zero'+ "\n") #if user tries to divide by zero
    else:
        answer= a/b
        print(str(a) + "/" + str(b) + "=" + str(answer)+"\n") #used concatenation to display answer
    





while True:
    print ("A. Addition")
    print("B.Subtraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.Exit")
    
    #Request user to select one of the above options
    choice = input("input your choice: ")


    #code which defines how the program responds to each option
    if choice == 'a' or choice == 'A':
        print("Addition")
        a= int(input('input first number:'))
        b=int(input('input second number: '))
        add(a,b)
    
    
    elif choice == 'b' or choice == 'B':
        print("Subtraction")
        a= int(input('input first number:'))#prompts user to input number and converts to data type int
        b=int(input('input second number: '))
        sub(a,b)
    
    elif choice == 'c' or choice == 'C':
        print("Multiplication")
        a= int(input('input first number:'))
        b=int(input('input second number: '))
        mul(a,b)
    
    elif choice == 'd' or choice == 'D':
        print("Division")
        a= int(input('input first number:'))
        b=int(input('input second number: '))
        div(a,b)
    
    elif choice == 'e' or choice == 'E':
        print("program ended")
        quit()


 
