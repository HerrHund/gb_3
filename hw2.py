#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.

firstName = input('your first name: ')
secondName = input('your second name: ')
yearsOld = input('year in which you were born: ')
city = input('your city: ')
email = input('your email: ')
phone = input('your phone: ')


def userInfo(a, b, c, d, e, f):
    print('user: ' + a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f)

userInfo(firstName, secondName, yearsOld, city, email, phone)
