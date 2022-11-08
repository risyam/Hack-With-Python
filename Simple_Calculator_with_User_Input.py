#! /bin/python3

num1=float(input("Enter first number"))
op=input("Enter Operator")
num2=float(input("Enter second number"))

# print(num1 + num2)

if op =="+":
    # print(num1+""+op+""+num2+"="+num1+num2)
    print(f"{num1}  {op} {num2} = {num1+num2}")
elif op=="-":
    print(f"{num1}  {op} {num2} = {num1 - num2}")
elif op=="*":
    print(f"{num1}  {op} {num2} = {num1 * num2}")
elif op=="/":
    print(f"{num1}  {op} {num2} = {num1 / num2}")
elif op=="^" or op=="**":
    print(f"{num1}  {op} {num2} = {num1 ** num2}")
else:
    print("Unknown Operator")
