a=int(input("enter a number: "))
print(f"you entered: {a}")

b=int(input("How many numbers do you wish to print: "))
print(f"printing {b} even numbers after {a}")

num = a
for x in range(b):
  #  while num % 2 == 0:
    while num % 2 != 0:
        num += 1
    print(num)
    num += 1
