def iterativefunction(n):
    factorial = 1
    for i in range(n):
        factorial = factorial * (i + 1)
    return factorial
print (iterativefunction(5))

# n = 5
# n = [0,1,2,3,4]
#   i   factorial   *   (i + 1)
#   0   1           *   0 + 1   so factorial = 1
#   1   1           *   1 + 1   so factorial = 2
#   2   2           *   2 + 1   so factorial = 6
#   3   6           *   3 + 1   so factorial = 24
#   4   24          *   4 + 1   so factorial = 120
# Full of n = 5 times so program exit
#https://www.youtube.com/watch?v=kx6DfrYfWnQ