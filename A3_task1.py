def fact(num):
    if num==0:
        return 1
    else:
        result = 1
        for i in range(1,num+1):
            result *= i

        return result
num1 = int(input("Enter a number: "))
answer=fact(num1)
print(f"The factorial of {num1} is {answer}")