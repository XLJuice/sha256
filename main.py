import hashlib
a = input("Якщо потрібно зашифрувати натисніть 1, якщо потрібно порівняти натисніть 2: ")
if a == '1' :
    data = input('Введіть текст: ')
    result = hashlib.sha256(data.encode())
    output = (result.hexdigest())
    print("Ваш hash : "+ output)
if a == '2' :
    data= input('Введіть текст: ')
    hash = hashlib.sha256(data.encode())
    hashhex = (hash.hexdigest())
    print(hashhex)
    ihash = input('ВВедіть hash: ')
    if hashhex == ihash:
        print('Hash співпадає')
    else:
        print('Hash не співпадає')
