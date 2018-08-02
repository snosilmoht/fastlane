import os 


dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

#r'C:\Users\dave\Repos\fastlane\game'  #os.path.dirname(os.path.dirname(__file__))
import sys
if dir_path not in sys.path:
    sys.path.append(dir_path)

for p in sys.path:
    print p
import core


if __name__ == '__main__':
    core.SimpleGame() #  .Work

else:
    print "error initializing"

