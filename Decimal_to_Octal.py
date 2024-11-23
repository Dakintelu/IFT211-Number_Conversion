num = int(input("Enter your Number: "))

octal = []
while num!=0:
    if num%8==1:
        num = (num-1)/8
        octal.insert(0,1)
    elif num%8==2:
        num = (num-2)/8
        octal.insert(0,2)
    elif num%8==3:
        num = (num-3)/8
        octal.insert(0,3)
    elif num%8==4:
        num = (num-4)/8
        octal.insert(0,4)
    elif num%8==5:
        num = (num-5)/8
        octal.insert(0,5)
    elif num%8==2:
        num = (num-6)/8
        octal.insert(0,6)
    elif num%8==2:
        num = (num-7)/8
        octal.insert(0,7)
    elif num%8==0:
        num = num/8
        octal.insert(0,0)

print("The Octal Number is: ",octal)