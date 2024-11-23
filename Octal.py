num = list(input("Enter the Octal Number: "))
total = 0
char = len(num)

for i in range(char):
    l_element = num.pop()
    if l_element=="1":
        total += (8 ** i) * 1
    elif l_element=="2":
        total += (8 ** i) * 2
    elif l_element=="3":
        total += (8 ** i) * 3
    elif l_element=="4":
        total += (8 ** i) * 4
    elif l_element=="5":
        total += (8 ** i) * 5
    elif l_element=="6":
        total += (8 ** i) * 6
    elif l_element=="7":
        total += (8 ** i) * 7
    elif l_element=="0":
        total += (8 ** i) * 0

print("Your Decimal Number is: ",total)
hexa = hex(total)[2:]
print("Your Hexadecimal Number is: ",hexa)
bina = bin(total)[2:]
print("Your Binary Number is: ",bina)