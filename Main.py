import math
import os.path
from os import path
import os

"""Sums the number from the user until he writes 'Stop' """


def fun_1():
    lst = []
    number = input("Enter a number to the list or write 'Stop' to stop\n")
    while number != 'Stop':
        lst.append(int(number))
        number = input()
    num_sum = sum(lst)
    print(num_sum)


"""Tic Tac Toe Game"""
"""Function has a tic tac toe board, if the game has a winner, it returns his number,
If its a draw, it will return 3, if its none of the above it will return -1"""


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
            """Checks for a Row winner"""
            if a[row][col] != a[row][0]:
                winner = False
            """Checks for a Col winner"""
            if a[col][row] != a[0][row]:
                winner2 = False
            """Checks for a draw"""
            if a[row][col] == 0:
                tie_check = False
        """Checks for a main diagonal winner"""
        if a[row][row] != a[0][0]:
            winner3 = False
        """Checks for a opposite diagonal winner"""
        if a[2 - row][row] != a[0][2]:
            winner4 = False
        """Checks for a Row winner"""
        if winner and a[row][0] != 0:
            return a[row][0]
        """Checks for a Col winner"""
        if winner2 and a[0][row] != 0:
            return a[0][row]
    """Checks for a main diagonal winner"""
    if winner3 and a[0][0] != 0:
        return a[0][0]
    """Checks for a opposite diagonal winner"""
    if winner4 and a[0][2] != 0:
        return a[0][2]
    """Checks for a draw"""
    if tie_check:
        return 3
    return -1


"""This function compresses a string and returns it
For example: abcaadddcc will be a1b1c1a2d3c2"""


def fun_3():
    print("Enter a string to compress")
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
    return result


"""This function checks if a number is an Israeli ID
If it is, return True, else return False"""
def fun_4():
    print("Enter an ID")
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
        """Reduces the sum from the closest round number up"""
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

"""This function gets a list and a function, and returns the list after the function that was given ran over 
all of the list's vars """
def fun_5(list, func):
    for i in range(len(list)):
        list[i] = func(list[i])
    return list


def square(x):
    return math.sqrt(x)





"""This function multiply the numbers it was given, but if the multiplication was already done in the past
it will not do the multiplication, but return the result it from a saved result"""
def fun_6(x, y):
    """If the file exists, open it, else, create it and open it"""
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
                """If the two first words are the two given number, return the third word = the result"""
                if int(words[0]) == x and int(words[1]) == y:
                    return words[2]
    print("message was not found in database")
    """If it was not found, multiply and save the result"""
    file.close()
    result = x * y
    file = open("Cache.txt", "a")
    file.write(" \n")
    file.write(str(x) + " " + str(y) + " " + str(result))
    file.close()
    return result

flag = True
while flag:
    print("Choose a function to run: ")
    print("1, 2, 3, 4, 5, 6 or 7 to stop")
    try:
        var = int(input())
        if var == 1:
            fun_1()
        elif var == 2:
            print(fun_2())
        elif var == 3:
            print(fun_3())
        elif var == 4:
            print(fun_4())
        elif var == 5:
            print(fun_5([25, 36, 49, 81], square))
        elif var == 6:
            print(str(fun_6(50, 20)))
        elif var == 7:
            flag = False
        else:
            print("Please enter a number from the given list!\n")
    except:
        print("Enter a number!")




