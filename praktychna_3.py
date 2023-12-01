import random
print("Відгадайте число!")
a = random.randint(1, 100)
while True:
    b = int(input("Введіть число: "))
    if b == a:
        print(f"Вітаємо, ви відгадали число: {a}")
    elif b < a:
        print("Більше!")
    else:
        print("Менше!")
print("Гра завершена!")
