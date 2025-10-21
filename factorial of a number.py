def factorial(x):
    if x==0 or x==1:
        return 1
    else:

        return x*factorial(x-1)
x=int(input(" enter your number : "))
if (x<0):
    print("factorial of negetive number is invalid")
else:

 print(f" the factorial of {x} is : {factorial(x)}")
