def select_task():
    task = input("Виберіть завдання: 1-5 або 'exit' для виходу: ")
    match task:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case "exit":
            exit()
        case _:
            print("Невірний вибір, спробуйте ще раз")
            select_task()

# Завдання 1
def task1():
    numbers_str = input("Введіть числа через пробіл: ").split()
    numbers = [int(n) for n in numbers_str]
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    print(f"Сума: {total}, Середнє арифметичне: {avg}")

# Завдання 2
def task2():
    numbers_str = input("Введіть числа через пробіл: ").split()
    numbers = [int(n) for n in numbers_str]
    x = int(input("Введіть число для перевірки: "))
    count = 0
    for n in numbers:
        if n == x:
            count += 1
    print(f"Число {x} зустрічається {count} раз(и)")

# Завдання 3
def task3():
    numbers_str = input("Введіть числа через пробіл: ").split()
    numbers = [int(n) for n in numbers_str]
    positive_sum = 0
    for n in numbers:
        if n > 0:
            positive_sum += n
    print(f"Сума додатніх чисел: {positive_sum}")

# Завдання 4
def task4():
    numbers_str = input("Введіть числа через пробіл: ").split()
    numbers = [int(n) for n in numbers_str]
    even_indices = []
    for i, n in enumerate(numbers):
        if n % 2 == 0:
            even_indices.append(i)
    print(f"Індекси парних чисел: {even_indices}")

# Завдання 5
def task5():
    numbers_str = input("Введіть числа через пробіл: ").split()
    numbers = [int(n) for n in numbers_str]
    seen = set()
    result = []
    for n in numbers:
        if n not in seen:
            result.append(n)
            seen.add(n)
    print(f"Список без повторів: {result}")

while True:
    select_task()
