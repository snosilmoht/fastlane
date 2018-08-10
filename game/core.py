import os
import json
import helpers


'''
to do:

 --- functions to handle weeks, months, years, triggers for each
 --- add more unit tests
 ----- fix error on bad commands
 --- build jobs dictionary (= save file)
 --- apply for job function
 --- work function
 --- relax function
 --- shop functions

 --- locations:
        locations are currently only loaded from locs1.fll file, need to turn
        those locations into actual locations with classes eventually:

     --- function to create locations based on location file (locs1.fll)
     --- function to create classifieds based on locations (instead of loading from locs.fll)
     --- need to save locations/classifieds information to location file (locs1.fll)



add race, age to character attribs


'''

class build():
    def __init__(self, title = 'build game'):
        print 'build game initiated'
        self.run()

    def run(self):
        qRun = raw_input("press n for new game, l for load game: ")
        print qRun

        if qRun.lower() == 'n':
            self.new_game()

        if qRun.lower() == 'l':
            self.load_game()

    def load_game(self):
        print 'load game'
        self.game = Game()
        self.game.load()

    def new_game(self):
        print 'new game'
        self.game = Game()
        self.game.setup()


class Game():
    def __init__(self, chars = [], weekNb = 1, timer = 0):
        self.characters = chars
        self.week = weekNb
        self.timer = timer

    def setup(self):
        print 'setting up game'

        nbChars = helpers.input_integer('Number of Players: ')

        for i in range(nbChars):
            charName = raw_input('character name: ')
            self.characters.append(Character(charName))


        self.run_game()

        return True

    def createLocations(self):
        return True

    def print_functions(self):
        self.help()
        return True

    def run_game(self):
        print "running game"
        self.run_week()

    def run_week(self):
        print "run week"
        self.timer = 0

        self.build_classifieds()

        for character in self.characters:
            self.current_character = character
            print "-------------{}'s turn".format(character.name)
            while self.timer < 12:
                action = helpers.interpreter(self, raw_input('enter action: '))

    def help(self):
        print helpers.get_functions(self)
        return True

    def save(self):
        #  save game settings
        saveName = '.'.join([raw_input("name of save file: "), 'fst'])#'testSave.fst'

        saveFile = helpers.get_relative_file('saves', saveName)

        '''
        relativePath = os.path.dirname(os.path.abspath(__file__))
        saveDir = os.path.join(relativePath, 'saves')


        saveFile = os.path.join(saveDir, saveName)
        '''
        saveData = {'week' : self.week,
                    'timer' :  self.timer
                    }

        saveData['character'] = []
        
        for char in self.characters:
            saveData['character'].append(char.save())

        print 'saving to {}'.format(saveFile)
        with open(saveFile, 'w') as outfile:
            json.dump(saveData, outfile)

    def load(self):
        loadName = 'testSave.fst'
        loadFile = helpers.get_relative_file('saves', loadName)

        print "_______loading {}".format(loadFile)

        with open(loadFile) as json_file:
            gameData = json.load(json_file)
        
        self.week = gameData['week']
        self.timer = gameData['timer']

        for char in gameData['character']:
            newChar = Character()
            newChar.load(char)
            self.characters.append(newChar)

        self.run_game()

    def info(self):
        if self.current_character:

            print 'Name:       {}'.format(self.current_character.name)
            print 'Savings:    {}'.format(self.current_character.savings)
            print 'Salary:     {}/hr'.format(self.current_character.salary)
            print 'Job:        {}'.format(self.current_character.job)
            print 'Edu.level:  {}'.format(self.current_character.education)
        else:
            print "no character intialized"

        print self.classifieds.keys()


        return True

    def work(self):
        self.timer += 1

    def apply_for_job(self):
        '''
        return True
        '''

        #  Display Classifieds
        for location in self.classifieds:
            print location
            for job in self.classifieds[location]['job']:
                print "  {}".format(job)


        #  Get valid location input

        inLoc = raw_input("where do you want to work? ")
        validLoc = [loc for loc in self.classifieds.keys() if loc.lower() == inLoc.lower()]
        if len(validLoc) == 0:
            print 'Error: not a valid location'
            self.apply_for_job()

        else:
            validLoc = validLoc[0]

        
        #  Get valid job input

        inJob = raw_input('what job? ')
        
        validJob = [job for job in self.classifieds[validLoc]['job'].keys() if job.lower() == inJob.lower()][0]

        if len(validJob) == 0:
            print "Error: not a valid job"
            self.apply_for_job()


        goalJob = self.classifieds[validLoc]['job'][validJob]

        if self.current_character.appearance < goalJob['minApp']:
            print "you did not get the job, need better appearance."
            return None

        elif self.current_character.education < goalJob['minEdu']:
            print "you did meet the minimum education requirements."
            return None

        else:
            self.current_character.job = goalJob['title']
            self.current_character.salary = goalJob['salary']
            return True



    def build_classifieds(self):
        print '-----building classfieds'
        jobsFile = helpers.get_relative_file('saves', 'locs1.fll')

        with open(jobsFile) as json_file:
            self.classifieds = json.load(json_file)
        





class SimpleGame():
    '''
    DEPRECATED, FOR REFERENCE ONLY!!!
    JUST A TEST
    '''
    def __init__(self, weekNb = 1, workWeek = 12, timer = 0, gameOver = False):
        self.week = weekNb
        self.workWeek = workWeek
        self.timer = 0 #  self.workWeek

        self.setup(loadGame)

        while self.week <= 3:
            self.curJobs = classifieds()
            self.player.classifieds = self.curJobs
            print "_____Week {} _____".format(self.week)
            self.player.timer = 0 #  self.workWeek
            self.runWeek()
            self.week += 1

        print "game over"

    def setup(self, loadGame = False):

        if loadGame:

            print 'load game'

            charName = 'do'
        else:

            print "____new game"
            charName = raw_input("enter your name: ")


        self.curJobs = classifieds()
        self.player = Character(
                                name = charName,
                                time = self.timer,
                                currentJobs = self.curJobs,
                                speedMultiplier = .33,
                                salary = 15,
                                workWeek = self.workWeek
                                )



        self.actionInterpreter()

    def actionInterpreter(self):
        '''
        builds dictionary to interpret simple commands into character commands
        '''

        self.actionDict= {}
        method_list = [func for func in dir(self.player) if callable(getattr(self.player, func)) and not func.startswith("__")]

        for method in method_list:
            self.actionDict[method] = "self.player.{}()".format(method)#self.player.__dict__[method]

        return True


    def runWeek(self):
        '''
        the basic work week function that runs
        '''
        self.timer = 0
        while self.timer < self.workWeek:
            act = raw_input("enter command: ")
            if act:

                if 'help' in act.lower():
                    self.userHelp()
                    return False

                elif 'debug' in act.lower():
                    self.userDebug()
                    return False
                elif 'quit' in act.lower():
                        quit()
                        break

                else:
                    act = [key for key in self.actionDict.keys() if key.lower() == act.lower()][0]

                    if not act:
                        print "improper command"

                    exec(self.actionDict[act])
                    print "savings: {}".format(self.player.savings)

            self.timer = self.player.timer
                    #print self.actionDict[act]
        #if self.timer <= 0:
        #    self.week += 1
        return True

    def userHelp(self):
        print "__________________help__________________"
        print "____actions"
        method_list = [func for func in dir(self.player) if callable(getattr(self.player, func)) and not func.startswith("__")]
        for method in method_list:
            print method

    def userDebug(self):
        print "__________________debug__________________"
        print "____actions"
        method_list = [func for func in dir(self.player) if callable(getattr(self.player, func)) and not func.startswith("__")]

        for method in method_list:
            print method
        print ""
        print "____player stats"
        for stat in  self.player.__dict__.keys():
            if stat != 'classifieds':
                print "{0}:  {1}".format(stat, self.player.__dict__[stat])

        print ""
        print "____classifieds"
        for key in self.curJobs.jobs:
            print key, self.curJobs.jobs[key]


class classifieds():
    def __init__(self):
        self.jobs = {'McDonalds' : 
                        {
                        'Cook':
                                {
                                 'title': 'Cook',
                                 'salary': 10,
                                 'prestige': 1,
                                 'minApp': 0,
                                 'minEdu': 0
                                },
                        'Supervisor':
                                {
                                 'title': 'Supervisor',
                                 'salary': 12,
                                 'prestige': 2,
                                 'minApp': 0,
                                 'minEdu': 1
                                },
                        'Manager':
                                {
                                 'title': 'Manager',
                                 'salary': 15,
                                 'prestige': 3,
                                 'minApp': 1,
                                 'minEdu': 2
                                },
                        'Owner':
                                {
                                 'title': 'Owner',
                                 'salary': 25,
                                 'prestige': 5,
                                 'minApp': 2,
                                 'minEdu': 4
                                }
                    }}



    def listJobs(self):
        print "listing jobs"
        for location in self.jobs.keys():
            print location
            #for job in self.jobs[location]
            #    print job #  , self.jobs[key]

    def applyForJob(self, job = None, appearance = 0):
        if job == None:
            "please select a job"
            return None

        else:
            print "you selected {}".format(job)

            if appearance < self.jobs[job]['minApp']:
                print "you did not get the job, need better appearance"
                return None
            else:
                print 'you got hired as {0}, with a salary of {1}'.format(job, self.jobs[job]['salary'])
                return self.jobs[job]



class Character():
    def __init__(   self,
                    name = None,
                    time = 12.0,
                    apartment = None,
                    hungry = False,
                    appearance = 0,
                    job = None,
                    salary = 0.00,
                    savings = 0.00,
                    education = 0,
                    speedMultiplier = 1,
                    workWeek = 12):

        self.name = name
        self.timer = time
        self.house = apartment
        self.hungry = hungry
        self.appearance = appearance
        self.job = None #currentJobs.jobs['McDonalds']['Cook']#job
        self.speed = 14.28
        self.salary = salary
        self.savings = savings
        self.education = education
        self.workWeek = 12#workWeek




    def relax(self):
        '''
        generic action to just take up time
        '''
        print "timer reduced by {} hours".format(self.speed)
        self.timer = self.timer + self.speed
        self.showCounter()

    def showCounter(self):
        print 'you have {} hours left'.format((self.workWeek - self.timer))

    def applyForJob(self):
        jobsDict = self.classifieds.jobs

        for location in jobsDict:
            print location
            for job in jobsDict[location]:
                print "  {}".format(job)


        inLoc = raw_input("where do you want to work? ")
        validLoc = [loc for loc in jobsDict.keys() if loc.lower() == inLoc.lower()]
        if not validLoc:
            print 'Error: not a valid location'
            self.applyForJob()

        validLoc = validLoc[0]

        
        inJob = raw_input("what job do you want to apply for? ")
        validJob = [job for job in jobsDict[validLoc].keys() if job.lower() == inJob.lower()]
        if not validJob:
            print "Error: not a valid job"
            self.applyForJob()

        else:
            validJob = validJob[0]
            goalJob = jobsDict[validLoc][validJob]

            #  check for minimum requirements for jobs

            if self.appearance < goalJob['minApp']:
                print "you did not get the job, need better appearance."
                self.timer = self.timer - .25
                return None


            elif self.education < goalJob['minEdu']:
                print "you did meet the minimum education requirements."
                self.timer = self.timer - .25
                return None

            else:
                print 'you got hired as {0}, with a salary of {1}'.format(validJob, jobsDict[validLoc][validJob]['salary'])
                self.job = jobsDict[validLoc][validJob]
                self.salary = self.job['salary']

        if not self.job:
            print "you are now still unemployed."

        self.timer = self.timer - .25

    def work(self):
        #print "working"
        if not self.job:
            print "you don't have a job yet!"

        else:
            self.timer = self.timer + (1*self.speed)
            if self.timer < self.workWeek:
                self.savings = self.salary + self.savings

            elif self.timer > self.workWeek:
                overage = abs(self.workWeek - self.timer)
                print "overage by {} hours".format(overage)
                self.savings = self.savings + (self.salary * overage)
                #self.timer = 0

            self.showCounter()

    def save(self):
        charData = {}

        charData['name'] = self.name
        charData['job'] = self.job
        charData['savings'] = self.savings
        charData['salary'] = self.salary
        charData['education'] = self.education

        return charData

    def load(self, data):
        self.name = data['name']
        self.job = data['job']
        self.savings = data['savings']
        self.salary = data['salary']
        self.education = data['education']
        return




'''
class oldCharacter():
    def __init__(   self,
                    name = "joe",
                    currentJobs = None,
                    time = 12.0,
                    apartment = None,
                    hungry = False,
                    appearance = 0,
                    job = None,
                    salary = 0.00,
                    savings = 0.00,
                    education = 0,
                    speedMultiplier = 1,
                    workWeek = 12):

        self.name = name
        self.classifieds = currentJobs
        self.timer = time
        self.house = apartment
        self.hungry = hungry
        self.appearance = appearance
        self.job = None #currentJobs.jobs['McDonalds']['Cook']#job
        self.speed = 14.28
        self.salary = salary
        self.savings = savings
        self.education = education
        self.workWeek = 12#workWeek


    def relax(self):
        print "timer reduced by {} hours".format(self.speed)
        self.timer = self.timer + self.speed
        self.showCounter()

    def showCounter(self):
        print 'you have {} hours left'.format((self.workWeek - self.timer))

    def applyForJob(self):
        jobsDict = self.classifieds.jobs

        for location in jobsDict:
            print location
            for job in jobsDict[location]:
                print "  {}".format(job)


        inLoc = raw_input("where do you want to work? ")
        validLoc = [loc for loc in jobsDict.keys() if loc.lower() == inLoc.lower()]
        if not validLoc:
            print 'Error: not a valid location'
            self.applyForJob()

        validLoc = validLoc[0]

        
        inJob = raw_input("what job do you want to apply for? ")
        validJob = [job for job in jobsDict[validLoc].keys() if job.lower() == inJob.lower()]
        if not validJob:
            print "Error: not a valid job"
            self.applyForJob()

        else:
            validJob = validJob[0]
            goalJob = jobsDict[validLoc][validJob]

            #  check for minimum requirements for jobs

            if self.appearance < goalJob['minApp']:
                print "you did not get the job, need better appearance."
                self.timer = self.timer - .25
                return None


            elif self.education < goalJob['minEdu']:
                print "you did meet the minimum education requirements."
                self.timer = self.timer - .25
                return None

            else:
                print 'you got hired as {0}, with a salary of {1}'.format(validJob, jobsDict[validLoc][validJob]['salary'])
                self.job = jobsDict[validLoc][validJob]
                self.salary = self.job['salary']

        if not self.job:
            print "you are now still unemployed."

        self.timer = self.timer - .25

    def work(self):
        #print "working"
        if not self.job:
            print "you don't have a job yet!"

        else:
            self.timer = self.timer + (1*self.speed)
            if self.timer < self.workWeek:
                self.savings = self.salary + self.savings

            elif self.timer > self.workWeek:
                overage = abs(self.workWeek - self.timer)
                print "overage by {} hours".format(overage)
                self.savings = self.savings + (self.salary * overage)
                #self.timer = 0

            self.showCounter()

def loadGame():
    print 'hi'

class Job():
    def __init__(self, salary = 10, prestige = 1):
        self.salary = salary
        self.prestige = prestige

class Build():
    def __init__(self):
        self.null = None

    def buildGfx(self):
        self.Graphics = None

class Week():
    def __init__(self, week = 0):
        self.week = week
'''


class venue():
    def __init__(self, name = None, type = None, location = [0,0], jobs = None):
        self.name = None
        self.type = None
        self.location = location
        self.jobs = None
