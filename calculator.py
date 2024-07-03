# CODE FOR SIMPAL CALCULATOR IN PYTHON 

print("WELCOME TO OUR CALCULATOR")

num1 = float(input("first number is : "))
num2 = float(input("second number is : "))

print("SELECT AN OPRATION TO PERFORM : ")
print("1. ADD (+)")
print("2. SUBTRACTION (-)")
print("3. MULTIPLY (*)")
print("4. DIVIDE (/)")

opration = input()

if opration == "1":
    #code for ADD
    result = num1 + num2
    print(result)
elif opration == "2":
    #code for SUBTRACTION 
    result = num1 - num2
    print(result)    
elif opration == "3":
    #code for MULTIPLICATION
    result = num1 * num2
    print(result)    
elif opration == "4":
    #code for DIVISION
    result = num1 / num2
    print(result)    
else:
    print("Invalid Entry")  

        
