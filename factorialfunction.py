def factorialfunction(n):
    factorial = 1
    if n >= 1:
        for i in range (1, n + 1, 1):
            factorial = factorial * i        
            print("Factorial Of ",n , " Is : ",factorial)
        return factorial
    else:
        print ("Invalid Input Number")
n = int(input("Enter Number You Want To Calculate : "))
result = factorialfunction(n)
print("Final Factorial is: %d "% result)