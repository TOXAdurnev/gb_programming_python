# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return ''.join(chr(cnt) + ch for (ch, cnt) in lst)


def decode(encoded_text):
    chars = []
    a = iter(encoded_text)
    for (cnt, ch) in zip(a, a):
        chars.append(ch * ord(cnt))
    return ''.join(chars)


if __name__ == "__main__":
    word = "aaaaWWWrrrCCCbht"
    rle_text = encode(word)
    print(len(word))  # -> 32
    print(len(rle_text))  # -> 12
    print(decode(rle_text))  # -> "aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa"
