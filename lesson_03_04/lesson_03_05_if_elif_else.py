weather = input("Введите какая сегодня погода: 1 - хорошая/2 - плохая: ")

if weather == "1":
    print("Идем гулять!")
    print("Хорошо проведем время!")
    restaurant = input("По пути будет ресторан: 1 - да/2 - нет: ")
    if restaurant == '1':
        print(f'Скушаем стейк.')
    else:
        print(f'Скушаем то, что найдем.')
else:
    print('Пойдем в кино')
    print('Купим попкорн')
    print('Насладимся фильмом')
    print('Покушаем')
