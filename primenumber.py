num1 = int(input("Enter Your First Number : "))
num2 = int(input("Enter Yout Last Number : "))

result = []

for x in range(num1, num2 + 1):
    if x <= 1 :
        continue
    elif x <= 3 :
        result.append(x)
    elif x == 5 or x == 7:
        result.append(x)
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        continue
    elif x % 5 == 0:
        continue
    elif x % 7 == 0 :
        continue
    else:
        result.append(x)


print(result)