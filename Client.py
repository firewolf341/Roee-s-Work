import socket

"""Ask the server if the ID exists"""
def CheckID(ID, s):
    message = "0 " + str(ID)
    s.send(message.encode())
    data = s.recv(1024)
    if data.decode() == "True":
        return True
    else:
        return False

"""Ask the server if the PIN is correct"""
def PinCheck(pin,s):
    message = "4 " + str(pin)
    s.send(message.encode())
    data = s.recv(1024)
    if data.decode() == "True":
        return True
    else:
        return False

"""Gets function code, info and socke, and reformats the message and sends it"""
def ReformatFileAndSend(code, amount, s):
    message = str(code + " " + amount)
    s.send(message.encode())


flag = True
"""Local IP address and random port number"""
HOST = '127.0.0.1'
PORT = 9876
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    print("Hello and welcome to Roee's ATM!")
    while flag:
        print("Please enter your ID: ")
        try:
            ID = int(input())
            if CheckID(ID, s):
                print("Please enter your pin code:")
                try:
                    val = int(input())
                    if PinCheck(val, s):
                        print("Welcome Back!")
                        while True:
                            print(
                                "Choose what do you want to do:\n1 - Pull Money\n2 - Deposit Money\n3 - See account info\n4 - To Exit\n")
                            info = input()
                            if int(info) == 1 or int(info) == 2:
                                while True:
                                    print("How Much Money?\n Insert Amount: ")
                                    amount = input()
                                    if int(amount) >= 0:
                                        ReformatFileAndSend(info, amount, s)
                                        data = s.recv(1024)
                                        if not data:
                                            break
                                        print("\n" + data.decode() + "\n")
                                        break
                                    else:
                                        print("\nPlease Enter a Valid Amount!")
                            elif int(info) == 3:
                                ReformatFileAndSend(str(info), str(0), s)
                                data = s.recv(1024)
                                if not data:
                                    break
                                print("\n" + data.decode() + "\n")

                            elif int(info) == 4:
                                print("Thank you for using Roee's ATM!")
                                flag = False
                                break
                            else:
                                print("Please enter a valid number!\n")
                    else:
                        print("Try Again!")
                except:
                    print("That's not a valid number!")


            else:
                print("\nCould not locate you in the database!\n")
        except:
            print("That's not a valid number!")
except:
    print("Server is offline")
