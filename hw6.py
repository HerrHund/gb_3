#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
# но каждое слово должно начинаться с заглавной буквы. 
# Необходимо использовать написанную ранее функцию int_func().

def upperWord(word):
    up = word
    firstLet = up[0][:1].upper()
    otherLet = up[1:]
    normalWord = firstLet + otherLet
    print(normalWord)

upperWord(input('word is: '))

def upperWords(words):
    strWords = words.split(' ')
    for wordI in strWords:
        strWord = str(wordI)
        firstLet = strWord[:1].upper()
        word = firstLet + strWord[1:]
        print(word)
   
        
upperWords(input('words is: '))