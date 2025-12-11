a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
c = float(input("enter the third  number:"))
d = float(input("enter the fourth  number:"))
sum_1 = a + b
sum_2 = c + d
if sum_2 != 0:
    res = sum_1 / sum_2
    print(f"The final result: {res:.2f}")
else:
    print("Error!")