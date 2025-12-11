a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
result = int((a % b == 0) | (b % a == 0))
print(result)