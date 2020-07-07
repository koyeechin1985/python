def recursivefunction(n):
    if n == 1:
        return 1
    else:
        result = n * recursivefunction(n - 1)
        return result
print(recursivefunction(5))

# n = 5
# n * factorial(n - 1)
# 5 * factorial(5 - 1) so 5 * factorial(4)                  
#    4 * factorial(4 - 1) so 4 * factorial(3)                
#       3 * factorial(3 - 1) so 3 * factorial(2)
#           2 * factorial(2 - 1) so 2 * factorial(1)
#                    factorial(1) = 1 because n == 1 return 1

#https://www.youtube.com/watch?v=kx6DfrYfWnQ

