digit = int(input())
i = 2
while i <= int(digit**(1/2)):
    if digit%i==0:
        print(str(digit) + " - Не простое число")
        break
    i+=1
else:
    print(str(digit) + " - Простое число")