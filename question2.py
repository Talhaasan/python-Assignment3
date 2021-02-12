class Ali:
    def __init__(self,messageSent):
        self.messageSent=messageSent

    def sendMessage(self):
        print("Sending message from Ali : " + str(self.messageSent))
class Veli:
    def __init__(self,isMessageConvenient,messageReceived):
        self.messageReceived = messageReceived
        self.isMessageConvenient = isMessageConvenient

    def showDisplay(self):
        if self.isMessageConvenient==True:
            print("Message received from Veli : " + str(self.messageReceived))
            print("Message has been read from Veli.")
            print("Veli's answer is :" + " I received your " + str(self.messageReceived))
            self.messageReceived = ""
        else:
            print("Message is inconvenient.")
class Server:
    def __init__(self,messageSent):
        if messageSent == "":
            self.isMessageConvenient = False
        else:
            self.isMessageConvenient = True
        self.messageSending = messageSent

    def isMessageConveniently(self):
        print("Message Conveniently Situation : " + str(self.isMessageConvenient))

import random
numberOfMessages = random.randint(0,10)
for i in range(numberOfMessages):
    inputMessage = random.choice(["Message " + str(i+1)])
    aliMessage = Ali(inputMessage)
    aliMessage.sendMessage()

    serverMessage = Server(aliMessage.messageSent)
    serverMessage.isMessageConveniently()

    veliMessage = Veli(serverMessage.isMessageConvenient,serverMessage.messageSending)
    veliMessage.showDisplay()
    print()