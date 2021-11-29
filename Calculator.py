def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter your choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        a = float(input("Enter 1st number:"))
        b = float(input("Enter 2nd number:"))
       
        if choice == '1':
            print(a ,"+" , b , "=" , add(a,b))

        elif choice == '2':
            print(a, "-" , b , "=" , subtract(a,b))

        elif choice == '3':
            print(a, '*' , b , "=" , multiply(a,b))
        
        elif choice == '4':
            print(a , '/' , b , "=" , divide(a,b))

        
        next_calculation = input("Lets do another calculation? (yes/no):")
        if (next_calculation) == "no":
            break

    else:
        print("invalid input")