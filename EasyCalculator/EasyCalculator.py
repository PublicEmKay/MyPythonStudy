#Простий калькулятор з мінімальним функціоналом, 
#виконаний через термінал
from colorama import init
from colorama import Fore, Back, Style

init()

print(Back.GREEN)
print(Fore.BLACK)
what = input("Що робимо? (+ - * /):\n")

a = float(input("Введіть перше число:\n"))
b = float(input("Введіть друге число:\n"))

print(Back.LIGHTBLUE_EX)
print(Fore.BLACK)

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
    print(Back.RED)
    print(Fore.BLACK)
    print("Нажаль даний функціонал недоступний(")
