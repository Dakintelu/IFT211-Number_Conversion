num = list(input("Enter You Hexadecimal number: "))
char = len(num)
total = 0
for i in range(char):
    l_element = num.pop()
    if l_element == "1":
        total+=(16**i)*1
    elif l_element == "2":
        total += (16**i)*2
    elif l_element == "3":
        total += (16**i)*3
    elif l_element == "4":
        total += (16**i)*4
    elif l_element == "5":
        total += (16**i)*5
    elif l_element == "6":
        total += (16**i)*6
    elif l_element == "7":
        total += (16**i)*7
    elif l_element == "8":
        total += (16**i)*8
    elif l_element == "9":
        total += (16**i)*9
    elif l_element == "A":
        total += (16**i)*10
    elif l_element == "B":
        total += (16**i)*11
    elif l_element == "C":
        total += (16**i)*12
    elif l_element == "D":
        total += (16**i)*13
    elif l_element == "E":
        total += (16**i)*14
    elif l_element == "F":
        total += (16**i)*15
    elif l_element == "0":
        total += (16**i)*0
    elif l_element == "2":
        total += (16**i)*2

print("Your Decimal Number is: ",total)

octal = oct(total)[2:]
print("Your Octal Number is: ",octal)

bina = bin(total)[2:]
print("Your Binary Number is: ",bina)
