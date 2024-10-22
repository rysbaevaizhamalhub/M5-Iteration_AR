# Aizhamal Rysbaeva
# Oct 22, 2024

# a program that iterates the integers from 1 to 50
# print messages for multiples of 3 and 5

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both! ")
    elif num % 3 == 0:
        print("Divisible by three! ")
    elif num % 5 == 0:
        print("Divisible by five! ")
    else:
        print(num)
