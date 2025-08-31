import random


def get_random_gift(gifts: list) -> str:
    gift = random.sample(gifts, 1)[0]
    return gift


if __name__ == '__main__':
    gifts1 = ['барбариски', "мячик", "машинка", "конструктор"]
    gifts2 = ['леденцы', "мишка", "самолетик", "вертолетик"]
    while True:

        user_choice = input("Введите: 1 - для 1го списка; 2 - для 2го списка: 0 - для остановки: ")
        if user_choice == '0':
            break
        elif user_choice == '1':
            print(f'Ваш подарок: {get_random_gift(gifts1)}.')
        elif user_choice == '2':
            print(f'Ваш подарок: {get_random_gift(gifts2)}.')
        else:
            print("Неверная команда")
