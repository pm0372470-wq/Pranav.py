#PS4.txt
n = int(input("Enter N: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

n = int(input("Enter N: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)