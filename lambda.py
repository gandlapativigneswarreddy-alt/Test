num = int(input("Enter number :"))

fun = lambda num : num % 2==0

if fun(num):
    print("Even")
else:
    print("Odd")