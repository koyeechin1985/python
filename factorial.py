n = int(input("Enter Number You Want To Calculate : "))
factorial = 1
if n >= 1:
    for i in range (1, n + 1, 1):
        factorial = factorial * i
        print("Factorial Of ",n , " Is : ",factorial)
    print ("Final Factorial Is : %d" % factorial)
else:
    print ("Invalid Input Number")