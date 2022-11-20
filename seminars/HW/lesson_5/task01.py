# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_in = 'авв вттб гу у'

exception = 'абв'


def main():
    res = ''.join([i for i in text_in if i not in exception])

    # data = [i for i in text_in]
    # filter_text = list(filter(lambda x: x not in exception, data))
    # res = ''.join(filter_text)
    if __name__ == "__main__":
        main()
