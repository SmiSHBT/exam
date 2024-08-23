#1

# Напишите код который создает пирамиду
# из звездочек

#2

# напишите код который выводит площадь треугольника

#3

# создайте калькулятор которая передает ответы на другой файл но если файл отсутвует выводит "файл не найден или отсутвует"

#4

# напишите класс которая создает файл и закидывает туда все заданное

#5

# напишите код
# которое запрашивает у пользователя имя пользователя а так же пароль и сравнивает его с тем которое уже сущетвует
# 1
def print_pyramid(n):
    for i in range(1, n + 1):
       
        print(' ' * (n - i) + '*' * (2 * i - 1))


height = 5
print_pyramid(height)

# 2
def triangle_area(base, height):
    return 0.5 * base * height


base = float(input("Введите основание треугольника: "))
height = float(input("Введите высоту треугольника: "))
area = triangle_area(base, height)
print(f"Площадь треугольника: {area}")
# 3
def calculate_and_save(operation, a, b, filename):
    try:
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b != 0:
                result = a / b
            else:
                return "Деление на ноль!"
        else:
            return "Недопустимая операция!"
        
        with open(filename, 'a') as file:
            file.write(f"{a} {operation} {b} = {result}\n")
        return result

    except FileNotFoundError:
        return "Файл не найден или отсутствует"


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")
filename = "results.txt"

result = calculate_and_save(operation, a, b, filename)
print(result)
# 4
class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
        print(f"Контент записан в файл {self.filename}")


writer = FileWriter("example.txt")
writer.write_to_file("Это пример текста, записанного в файл.")
# 5

stored_username = "user1"
stored_password = "password123"


username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")


if username == stored_username and password == stored_password:
    print("Доступ разрешен.")
else:
    print("Неверное имя пользователя или пароль.")


