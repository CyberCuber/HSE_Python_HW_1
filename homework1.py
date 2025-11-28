# Домашнее задание 1 - Управляющие конструкции

# ===== ЗАДАНИЕ 1 =====
def find_middle_letters(word):
    # Находим среднюю букву в слове
    length = len(word)
    middle = length // 2
    
    if length % 2 == 1:  # если нечетное количество букв
        return word[middle]
    else:  # если четное количество
        return word[middle-1:middle+1]

# Проверка задания 1
print("Задание 1:")
print(f"test -> {find_middle_letters('test')}")
print(f"testing -> {find_middle_letters('testing')}")
print()

# ===== ЗАДАНИЕ 2 =====
def dating_service(boys, girls):
    # Проверяем, одинаковое ли количество
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары!")
        return
    
    # Сортируем и создаем пары
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    
    print("Идеальные пары:")
    for i in range(len(boys_sorted)):
        print(f"{boys_sorted[i]} и {girls_sorted[i]}")

# Проверка задания 2
print("Задание 2 - Пример 1:")
boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
dating_service(boys1, girls1)

print("\nЗадание 2 - Пример 2:")
boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'] 
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
dating_service(boys2, girls2)
