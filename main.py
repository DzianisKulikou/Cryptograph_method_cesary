
def cesar(symbol, mixing):
    ord_symbol = ord(symbol)
    if 65 <= ord_symbol <= 90:
        beginning = 65
        num = 26
    elif 97 <= ord_symbol <= 122:
        beginning = 97
        num = 26
    elif 1040 <= ord_symbol <= 1071:
        beginning = 1040
        num = 32
    elif 1072 <= ord_symbol <= 1103:
        beginning = 1072
        num = 32
    else:
        return symbol
    return chr(beginning + (ord(symbol) - beginning + mixing) % num)


text = input('Здравствуйте! Я помогу вам зашифровать(дешифровать) ваш текст шифром Цезаря!\n'
             'Введите текст для шифрования или дешифрования: ')
k = int(input('Введите цифру, на сколько символов мы должны сделать смещение. При дешифровании добавьте символ МИНУС '
              '(-) перед цифрой! : '))

for i in range(len(text)):
    print(cesar(text[i], k), end='')

print('\nВсё сделано!')
