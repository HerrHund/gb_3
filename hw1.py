#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
firstNum = int(input('first num: '))
secondNum = int(input('second num: '))


def delete(a, b):
    try:
        c = a // b
        print(c)

    except UnboundLocalError:
        print('Не делите на ноль')
        
        
    except ZeroDivisionError:
        print('Не делите на ноль')
        
        


delete(firstNum, secondNum)