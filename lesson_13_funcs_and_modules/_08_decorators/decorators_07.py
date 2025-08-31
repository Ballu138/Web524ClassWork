def authorise_admin(func):
    def wrapper(user):
        if user == 'admin':
            return func()
        else:
            print("Доступ запрещен!")

    return wrapper


@authorise_admin
def secret():
    print('Секретная информация!')


if __name__ == '__main__':
    secret('user')
    secret('admin')
