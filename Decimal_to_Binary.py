num = int(input("Enter your Number: "))

binary = []

while num != 0:
    if num % 2 == 0:
            num = num / 2
            binary.insert(0, 0)
    else:
            num = (num - 1) / 2
            binary.insert(0, 1)


print("Your Binary Number is: ", binary)

