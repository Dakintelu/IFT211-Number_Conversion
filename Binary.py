num = list(input("Enter you Binary Number: "))
total = 0
char = len(num)
for i in range(char):
    l_element = num.pop()
    if l_element=="1":
        total+=pow(2,i)
print("The Decimal Number is: ",total)

octal = oct(total) [2:]
print("The Octal Number is: ",octal)

hexa = hex(total)[2:]
print("The HexaDecimal is: ", hexa)

def binary_to_hex(num):
    return hex(int(num,2))