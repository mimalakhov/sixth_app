#First________________________________________________________________________
''' Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию. 
'''
def byte_encode(list):
    '''Прямая функция. Кодирует список строк'''
    encoded = []
    for i in range(len(list)):
        encoded.append(list[i].encode('utf-8'))
    return encoded

def byte_decode(list):
    '''Обратная функция'''
    decoded = []
    for i in range(len(list)):
        decoded.append(list[i].decode('utf-8'))
    return decoded

#Конкретные примеры
list1=['dfdsf', 'sdfdsfsd', 'bnkjo']
list2=[b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82']
print("Encoding: {}".format(byte_encode(list1)))
print("Decoding: {}".format(byte_decode(list2)))
print()

#Second_______________________________________________________________________________
''' Формула молекулы спирта - C2H5(OH). 
    Из неё видно, что молекула состоит из двух атомов углерода (С), 6 атомов водорода (Н) и одного атома кислорода (О). 
    В Input.txt содержится 3 натуральных числа: C, H, O – количество атомов углерода, водорода и кислорода соответственно. 
    В файл Output.txt вывести максимально возможное число молекул спирта, которые могут получиться из атомов, представленных во входных данных.
'''
def hangover(list):
    '''Функция принимает на вход список из трёх чисел и ищет минимум среди элементов, целочисленно поделенных на соответсвующие константы'''
    new_list=[list[0] // 2, 
              list[1] // 6, 
              list[2] // 1]
    return min(new_list)

#Ввод данных из файла со всеми проверками
try:
    with open('C:\\Users\\user\\Desktop\\input.txt', 'r') as f:
        C = int(f.readline())
        O = int(f.readline())
        H = int(f.readline())
        data=[C, O, H]
    with open('C:\\Users\\user\\Desktop\\output.txt', 'w') as f1:
        f1.write(str(hangover(data)))
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Wrong value!")

#Third_____________________________________________________________________________
'''XOR шифрование/расшифрование. 
   На входе файл с текстом и ключ шифрования (строка), на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.
'''
def xor(data, key): 
    '''Функция для кодирования информации'''
    str = ""
    return str.join(chr(ord(d) ^ ord(k)) for (d, k) in zip(data, key))

# Открытие и чтение из файла со всеми проверками
try:
    with open("C:\\Users\\user\\Desktop\\input-xor.txt", 'r') as f:
        key = str(f.readline())
        lines = f.readlines()
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Wrong value!")

data = "".join(c.strip() for c in lines)

#Последовательные вызовы функций и запись полученных данных в файл
encode_data = xor(data, key)
with open("C:\\Users\\user\\Desktop\\output-xor.txt", "w") as f:
    f.write(encode_data + '\n') 

decode_data = xor(encode_data, key)
with open("C:\\Users\\user\\Desktop\\output-xor.txt", "a") as f:
    f.write(str(decode_data))  