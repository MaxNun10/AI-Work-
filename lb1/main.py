
int_var = 10
float_var = 3.14
str_var = "Максим"
bool_var = True

print(int_var, type(int_var))
print(float_var, type(float_var))
print(str_var, type(str_var))
print(bool_var, type(bool_var))


a, b, c = 10, 5, 3
print(a + b, a - b, a * b, a / b, a ** b)
print(round(3.678, 2))
print(abs(-7))
print(a % c)
print((a + b + c) / 3)


name = "Максим"
age = 18
print("Привіт, мене звати " + name)
print(name.upper())
print(f"Мене звати {name}, мені {age} років")


test_num = int(input("Введіть число: "))
if test_num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

if 10 <= test_num <= 50:
    print("Число в діапазоні 10-50")
else:
    print("Число поза діапазоном")


for i in range(1, 11):
    print(i)

sum_num = 0
n = 1
while n <= 100:
    sum_num += n
    n += 1
print("Сума чисел від 1 до 100:", sum_num)


def add_numbers(x, y):
    return x + y

def reverse_string(s):
    return s[::-1]

print(add_numbers(3, 7))
print(reverse_string("Програмування"))


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
numbers.append(6)
numbers.pop()
print(numbers)


student = {"ім'я": "Максим", "вік": 18, "факультет": "Інженерія програмного забезпечення"}
print(student["ім'я"])
student["рік навчання"] = 3
print(student)


try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    result = num1 / num2
    print("Результат ділення:", result)
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
except ValueError:
    print("Помилка: введіть числове значення!")
