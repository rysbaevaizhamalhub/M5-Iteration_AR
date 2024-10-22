# Aizhamal Rysbaeva
# Oct 22, 2024

# Get a list of 10 numbers from random.org.
# Write code so that you loop through every number in the list
# print out a message dependent on whether the number is even or odd.


numbers = [33, 33, 1, 67, 65, 52, 31, 21, 49, 98]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is odd!")
