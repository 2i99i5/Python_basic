"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""


# работает для латиницы
def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    # если ничего не ввели
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        # для последнего набора символов
        enconding += str(count) + prev_char
        return enconding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            # в том числе и для чисел, состоящих из нескольких цифр
            count += char
        else:
            # умножение символа на число = повторение символа
            decode += char * int(count)
            count = ''
    return decode


if __name__ == "__main__":
    # ввод текста в файл
    with open('encode.txt', 'w', encoding='UTF-8') as file:
        file.write(input('Напишите текст для сжатия: '))

    # читаем и кодируем
    with open('encode.txt', 'r') as file:
        my_text = file.readline()
    print(f'введенный текст: {my_text}')

    encoded = rle_encode(my_text)
    with open('decode.txt', 'w', encoding='UTF-8') as file:
        file.write(f'{encoded}')
    print(f'закодированный текст: {encoded}')

    # читаем и декодируем
    with open('decode.txt', 'r') as file:
        my_text = file.readline()
    decoded = rle_decode(my_text)
    print(f'раскодированный текст: {decoded}')
