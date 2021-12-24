#Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

a = int(input('first num: '))
b = int(input('second num: '))
c = int(input('third num: '))

def higherSum(a, b, c):

    argsData = [a, b, c]
    argSum = []

    maxSum1 = max(argsData)
    argSum.append(maxSum1)

    argsData.remove(maxSum1)

    maxSum2 = max(argsData)
    argSum.append(maxSum2)

    print(sum(argSum))

higherSum(a, b ,c)