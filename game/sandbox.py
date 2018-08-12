import os
import json

def save():
    relativePath = os.path.dirname(os.path.abspath(__file__))
    saveDir = os.path.join(relativePath, 'saves')

    print saveDir

saveFolder = r'C:\Users\dave\Repos\fastlane\game\saves'

gameData = {}

gameData['weekNb'] = 2
gameData['timer'] = 5


class mycls():
    def __init__(self):
        self.attr1 = 'attribute 1'
        self.legs = 2
        self.someDict = {'key1': "balls_out!", 'response2': 'no way!'}
        #self.printShit()

    def printShit(self):
        funcs = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]

        for f in funcs:
            print f

    def anotherClass(self):
        print 'hello another class'

class gameClass():
    def __init__(self):
        characters = []
        self.clsInstance1 = mycls()
        self.clsInstance2 = mycls()

        self.clsInstance1.legs = 3
        self.clsInstance2.legs = 120

    def doShit(self):
        self.clsInstance2.attr1 = 'attribute 2'


def printkeys():
    print '--- keys ---'
    go = gameClass()

    print vars(go)
    for var in vars(go):
        print type(var)
    for key in vars(go).keys():
        print key

def printDict():
    print '--- __dict__ ---'
    gameInstance = gameClass()
    print gameInstance.__dict__

def multiText():
    slob = True
    idiot = True

    if slob or idiot:
        r = 'you are {slob}{also}{dumb}'.format(slob = 'a slob ' if slob else "",
                                                also = 'and ' if slob and idiot else "",
                                                dumb = 'dumb' if idiot else "")

        print r

def keys():
    myDict = {"key1": "fuck", 'key2': "shit"}
    return myDict

dic = keys()

print dic.keys()

