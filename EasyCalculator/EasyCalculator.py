#Простий калькулятор з мінімальним функціоналом, 
#виконаний через термінал

what = input("Що робимо? (+ - * /):\n")

a = float(input("Введіть перше число:\n"))
b = float(input("Введіть друге число:\n"))

if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
else:
    print("Нажаль даний функціонал недоступний(")