
print('''
      + add
      - subtract
      * multiply
      / divide''')
    
num1=int(input("enter the value1:"))
num2=int(input("enter the value 2:"))
operation=input("enter the operation:")
if operation=="+":
        print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("invalid operation")

    
