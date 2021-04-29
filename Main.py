import math
import os.path
from os import path
import os


def fun_1():
    lst = []
    number = input("Enter a number to the list or write 'Stop' to stop\n")
    while number != 'Stop':
        lst.append(int(number))
        number = input()
    num_sum = sum(lst)
    print(num_sum)


def fun_2():
    a = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 1]]
    tie_check = True
    winner3 = True
    winner4 = True
    for row in range(3):
        winner = True
        winner2 = True
        for col in range(3):
            if a[row][col] != a[row][0]:
                winner = False
            if a[col][row] != a[0][row]:
                winner2 = False
            if a[row][row] == 0:
                tie_check = False

        if a[row][row] != a[0][0]:
            winner3 = False
        if a[2 - row][row] != a[0][2]:
            winner4 = False
        if winner and a[row][0] != 0:
            return a[row][0]
        if winner2 and a[0][row] != 0:
            return a[0][row]
    if winner3 and a[0][0] != 0:
        return a[0][0]
    if winner4 and a[0][2] != 0:
        return a[0][2]
    if tie_check:
        return 3
    return -1


def fun_3():
    word = input()
    result = word[0]
    j = 0
    num = 0
    for i in range(len(word)):
        if result[j] is not word[i]:
            result += str(num)
            j += 2
            num = 0
            if i < len(word) - 1:
                result += word[i]
        num += 1
    result += str(num)


def fun_4():
    number = input()
    if len(number) == 9:
        bik = int(number[8])
        sum = 0
        for i in range(8):
            if i % 2 == 0:
                sum += int(number[i]) * 1
            else:
                num = int(number[i]) * 2
                if num > 9:
                    num = round((num / 10)) + (num % 10)
                sum += num
        sum = math.ceil(sum / 10.0) * 10 - sum

        if sum == bik:
            print("Valid")
            return True
        else:
            print("Not Valid")
            return False
    else:
        print("Not Valid")
        return False


def fun_5(list, func):
    for i in range(len(list)):
        list[i] = func(list[i])
    return list


def square(x):
    return math.sqrt(x)


print(fun_5([25, 36, 49, 81], square))


def fun_6(x, y):
    if path.exists('Cache.txt'):
        file = open("Cache.txt", "r")
    else:
        file = open("Cache.txt", "w")
        file.write("")
        file.close()
        file = open("Cache.txt", "r")

    for line in file:
        words = line.split()
        if words:
            if len(words) >= 3:
                if int(words[0]) == x and int(words[1]) == y:
                    return words[2]
    print("message was not found in database")
    file.close()
    result = x * y
    file = open("Cache.txt", "a")
    file.write(" \n")
    file.write(str(x) + " " + str(y) + " " + str(result))
    file.close()
    return result







