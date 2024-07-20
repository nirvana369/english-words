import sys


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def plus_cal(x):
    sum = 0
    for y in range(0, len(x)):
        sum += ord(x[y]) - 64
    return sum


def mul_cal(x):
    mul = 1
    for y in range(0, len(x)):
        mul *= ord(x[y]) - 64
    return mul


def search(x, plus, mul):
    p = plus_cal(x.upper())
    m = mul_cal(x.upper())
    if plus.get(p) != None and mul.get(m) != None:
        arr = []
        for i in plus[p]:
            if i in mul[m]:
                arr.append(i)
        return arr
    return ["not found"]


def process(params, plus, mul):
    for word in params:
        p = plus_cal(word.upper())
        m = mul_cal(word.upper())
        ret = search(word, plus, mul)
        print('-- Find by plus and multiply --')
        print(p)
        print(m)
        print(ret)
        print('=============================================================================================================')
        # print('-- Find by plus only --')
        # print(plus_cal(word.upper()))
        # print(plus[p])
        # print('=============================================================================================================')
        # print('-- Find by multiply only --')
        # print(mul_cal(word.upper()))
        # print(mul[m])
        # print('=============================================================================================================')
        

def main(params):
    english_words = load_words()
    plus = {}
    mul = {}

    for x in english_words:
        p = plus_cal(x.upper())
        m = mul_cal(x.upper())
        if plus.get(p) != None:
            plus[p].append(x)
        else:
            plus[p] = [x]

        if mul.get(m) != None:
            mul[m].append(x)
        else:
            mul[m] = [x]

    process(params, plus, mul)

if __name__ == '__main__':
    # list string - input from user
    main(sys.argv[1:])
