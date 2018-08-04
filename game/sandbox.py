import os
import json

saveFolder = r'C:\Users\dave\Repos\fastlane\game\saves'

gameData = {}

gameData['weekNb'] = 2
gameData['timer'] = 5


class mycls():
    def __init__(self):
        print 'class init'
        self.printShit()

    def printShit(self):
        funcs = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]

        for f in funcs:
            print f

    def anotherClass(self):
        print 'hello another class'

go = mycls()