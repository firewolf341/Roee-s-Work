import sys
import socket
import os.path
from os import path
import os


def SendMessage(message, connection):
    connection.send(message.encode())

""" Main Function that gets the correct
function for the client's request"""
def ATMJob(code, ID, info, file):
    if code == "0":
        return IDCheck(info, file)
    if code == "1":
        return PullMoney(info, ID, file)
    if code == "2":
        return DepositMoney(info, ID, file)
    if code == "3":
        return DisplayAccInfo(ID, file)
    if code == "4":
        return PINCheck(ID, info, file)
    return "False"

"""checks if the ID exists in the database"""
def IDCheck(ID, file):
    """check every line's first word for the ID"""
    for line in file:
        words = line.split()
        if words:
            if len(words) >= 1:
                if words[0] == ID:
                    return "True"
    return "False"

"""pulls money from the correct account"""
def PullMoney(Amount, ID, file):
    counter = 0
    """searches for the clients account, and pulls the money"""
    for line in file:
        words = line.split()
        if words:
            if len(words) >= 3:
                if words[0] == ID:
                    """if there's enough money in the bank account"""
                    if int(words[1]) >= int(Amount):
                        """Update the amount in the bank account"""
                        file.close()
                        file = open("Bank.txt", "r")
                        allLines = file.readlines()
                        allLines[counter] = (words[0] + " " + str(int(words[1]) - int(Amount)) + " " + words[2] + "\n")
                        file.close()
                        file = open("Bank.txt", "w")
                        file.writelines(allLines)
                        return "The money has been pulled successfully"
                    else:
                        return "Not enough money!"
        counter += 1
    return "Bank Account was not found"


"""Deposits money from the correct account"""
def DepositMoney(Amount, ID, file):
    counter = 0
    """searches for the clients account, and deposits the money"""
    for line in file:
        words = line.split()
        if words:
            if len(words) >= 3:
                if words[0] == ID:
                    """Update the amount in the bank account"""
                    file.close()
                    file = open("Bank.txt", "r")
                    allLines = file.readlines()
                    allLines[counter] = (words[0] + " " + str(int(words[1]) + int(Amount)) + " " + words[2] + "\n")
                    file.close()
                    file = open("Bank.txt", "w")
                    file.writelines(allLines)
                    return "The money has been deposited successfully!"
        counter += 1
    return "Bank Account was not found"

"""Returns the information of the client's account"""
def DisplayAccInfo(idOfClient, file):
    for line in file:
        words = line.split()
        if words:
            if len(words) >= 2:
                if words[0] == idOfClient:
                    return "ID of account holder:" + words[0] + "\nAmount of money left:" + words[1]
    return "Bank Account was not found"


"""Validates the PIN of the client's account"""
def PINCheck(ID, PIN, file):
    for line in file:
        words = line.split()
        if words:
            if len(words) >= 3:
                """"If it's the right account and the right PIN"""
                if words[0] == ID:
                    if words[2] == PIN:
                        return "True"
                    else:
                        return "False"
    return "False"

"""Creates a file if one doesn't exists"""
def FileExists():
    if not path.exists('Bank.txt'):
        file = open("Bank.txt", "w")
        file.write("")
        file.close()


"""Local IP address and random port number"""
HOST = '127.0.0.1'
PORT = 9876
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
while True:
    print("Server is running and waiting for a client!\n")
    conn, addr = s.accept()
    """When a client connects"""
    with conn:
        ID = 0
        print('Connected by', addr)
        while True:
            try:
                file = open("Bank.txt", "r+")
                """receive data from the client"""
                data = conn.recv(1024).decode()
                print("The client sent: " + data + "\n")
                if not data:
                    break
                """the data's first word will be the function code, then the info for it"""
                data = data.split()
                if len(data) >= 2:
                    code = data[0]
                    info = data[1]
                    result = ATMJob(code, ID, info, file)
                    """If this is a login call, remember the ID number"""
                    if result == "True" and code == "0":
                        ID = info
                    SendMessage(result, conn)
                else:
                    SendMessage("Error!", conn)
                file.close()
            except:
                print("Client", addr, "Disconnected")
                break
