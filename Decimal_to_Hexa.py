num = int(input("Enter your Number: "))

hexadecimal = []
while num != 0:
    if num % 16 == 1:
            num = (num - 1) / 16
            hexadecimal.insert(0, 1)
    elif num % 16 == 2:
            num = (num - 2) / 16
            hexadecimal.insert(0, 2)
    elif num % 16 == 3:
            num = (num - 3) / 16
            hexadecimal.insert(0, 3)
    elif num % 16 == 4:
            num = (num - 4) / 16
            hexadecimal.insert(0, 4)
    elif num % 16 == 5:
            num = (num - 5) / 16
            hexadecimal.insert(0, 5)
    elif num % 16 == 6:
            num = (num - 6) / 16
            hexadecimal.insert(0, 6)
    elif num % 16 == 7:
            num = (num - 7) / 16
            hexadecimal.insert(0, 7)
    elif num % 16 == 8:
            num = (num - 8) / 16
            hexadecimal.insert(0, 8)
    elif num % 16 == 9:
            num = (num - 9) / 16
            hexadecimal.insert(0, 9)
    elif num % 16 == 10:
            num = (num - 10) / 16
            hexadecimal.insert(0, "A")
    elif num % 16 == 11:
            num = (num - 11) / 16
            hexadecimal.insert(0, "B")
    elif num % 16 == 12:
            num = (num - 12) / 16
            hexadecimal.insert(0, "C")
    elif num % 16 == 13:
            num = (num - 13) / 16
            hexadecimal.insert(0, "D")
    elif num % 16 == 14:
            num = (num - 14) / 16
            hexadecimal.insert(0, "E")
    elif num % 16 == 15:
            num = (num - 15) / 16
            hexadecimal.insert(0, "F")
    elif num % 16 == 0:
            num = num / 16
            hexadecimal.insert(0, 0)


print("Your Hexadecimal Number is: ", hexadecimal)
