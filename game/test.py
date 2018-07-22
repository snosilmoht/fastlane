import core

def sasdsaimpleGame():
    print "test game"

    myName = raw_input("enter your name: ")
    player1 = core.Character(   name = myName,
                                speedMultiplier = .33)

    print "Character Created, hi {}!".format(player1.name)

    #print player1.__dict__.keys()

    while player1.timer > 0:
        act = input("enter command: ")



if __name__ == '__main__':
    core.SimpleGame().Work

else:
    print "error initializing"