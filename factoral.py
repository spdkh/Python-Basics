# Question 2:
# n * (n - 1) * (n - 2) * ... * (n == 1)

n = int(input())
x = 1
while n > 1:
    x = n * x
    n = n - 1
print(x)
