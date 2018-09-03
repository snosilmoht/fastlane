import os
import json
#import simplejson
import helpers


'''
to do:

 CURRENTLY
 ---FIND compound interest function that takes into account contributions/payments

 TO DO:
 --- proper fafsa formulas

 --- add more unit tests
 ----- fix error on bad commands
 --- build jobs dictionary (= save file)
 --- relax function
 --- shop functions
 --- health insurance!


 --- locations:
        locations are currently only loaded from locs1.fll file, need to turn
        those locations into actual locations with classes eventually:

     --- function to create locations based on location file (locs1.fll)
     --- function to create classifieds based on locations (instead of loading from locs.fll)
     --- need to save locations/classifieds information to location file (locs1.fll)
 
 --- add interest to loans


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
    def __init__(self, chars = [], weekNb = 1, timer = 0.0):
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
        while self.week < 144:
            self.run_week()

    def run_week(self):
        print "-------week number {}".format(self.week)
        self.build_classifieds()

        for character in self.characters:
            self.timer = 0
            self.current_character = character
            print "-------------{}'s turn".format(character.name)
            self.weekly_event()
            while self.timer < 12:
                action = helpers.interpreter(self, raw_input('enter action: '))
                self.displayTime()

            print "Week Over"

        self.week += 1

    def help(self):
        print helpers.get_functions(self)
        return True

    def save(self):
        #  save game settings
        saveName = '.'.join([raw_input("name of save file: "), 'fst'])#'testSave.fst'

        saveFile = helpers.get_relative_file('saves', saveName)

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
        loadName = 'dave_cheating.fst'
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

            print 'Name:            {}'.format(self.current_character.name)
            print 'Savings:         {}'.format(self.current_character.savings)
            print 'Salary:          {}/hr'.format(self.current_character.salary)
            print 'Job:             {}'.format(self.current_character.job)
            print 'Edu.level:       {}'.format(self.current_character.education)
            print 'Student Debt:    {}'.format(round(self.current_character.studentDebt, 2))
            print 'Student?:        {}'.format(self.current_character.student)
            if self.current_character.student:
                print 'CreditHours Left:{}'.format(self.current_character.studytime)
            print ''
            print 'week nb:         {}'.format(self.week)
        else:
            print "no character intialized"

        print self.classifieds.keys()


        return True

    def work(self):

        if not self.current_character.job:
            print 'you are unemployed!'
            return False

        t = self.do_hour()
        self.current_character.savings = self.current_character.savings + ((self.current_character.salary * 5) * t)
        
        self.timer += 1

    def study(self):
        if not self.current_character.student:
            print "you are not currently enrolled"
            return False
        
        time = self.current_character.studytime

        print "you are currently enrolled as: {}".format(self.current_character.student)
        print "you have {} hours left before your course is complete".format(time)
        self.timer = self.timer + 1
        studyTimer = 1
        overtime = None

        t = self.do_hour()

        self.current_character.studytime = time - (t * 5)

        if self.current_character.studytime <= 0:
            degree = self.classifieds['school']['level'][self.current_character.student]
            self.current_character.education = degree['outEdu']
            print "You graduated with a {}!".format(degree['nicename'])
            self.current_character.student = None
        print "You studied, you have {} hours left in your course".format(self.current_character.studytime)

    def do_hour(self):
        '''
        Adds one game hour and returns approprate overtime if necessary
        '''
        overtime = None
        workTimer = self.timer + 1

        if workTimer - 12.0 > 0:
            overtime = self.timer - 12.0
            print "overtime hours: {}"

        t = (overtime if overtime else 1)

        return t


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
        slob = False
        idiot = False

        if self.current_character.appearance < goalJob['minApp']:
            slob = True

        if self.current_character.education < goalJob['minEdu']:
            idiot = True


        if slob or idiot:
            print "you did not get the job"
            r = 'you are {slob}{also}{dumb}.'.format(slob = 'a slob ' if slob else "",
                                                    also = 'and ' if slob and idiot else "",
                                                    dumb = 'dumb' if idiot else "")

            print r
            self.timer += .25

            return False
            print "more...................."
        else:
            self.current_character.job = goalJob['title']
            self.current_character.salary = goalJob['salary']

            print "you got the job, you current position is {0}, you earn ${1}/hr".format(self.current_character.job,
                                                                                        self.current_character.salary)
            self.timer += .25
            return True

    def apply_for_school(self):
        degrees = self.classifieds['school']['level']

        for d in degrees.keys():
            print degrees[d]['degree']

        inDegree = raw_input("For which degree are you applying? " )

        self.validD = [d for d in self.classifieds['school']['level'].keys() if inDegree.lower() == d.lower()][0]

        if len(self.validD) == 0:
            print "Error: not a valid degree"
            self.apply_for_school()

        self.validD = self.classifieds['school']['level'][self.validD]

        if self.validD['requirement'] > self.current_character.education:
            print 'you do not meet the minimum educational requirement'
            return False

        costMsg = "This Degree will cost ${0}".format(self.validD['cost'])
        print costMsg
        
        if self.current_character.savings < self.validD['cost']:
            print 'You do not have enough savings to cover the tuition... '
            print ''
            yesLoan = raw_input("Would you like to take out a loan? (y/n) ")
            if yesLoan.lower == 'n':
                yesLoan = None

        if not yesLoan:
            print "Very well then, you walked away"
            return False

        else:
            self.apply_for_loan(self.validD['cost'])

        self.current_character.student = self.validD["degree"]
        self.current_character.studytime = self.validD['hours']


        '''
        ==================================================
        NEED TO FINISH THIS
        set character to 'student'
        able to study
        make study function
        =================================================
        '''


    def apply_for_loan(self, amount):
        '''
        FOR NOW, THIS IS JUST A PLACEHOLDER AS IF YOU GOT THE LOANS
        NEED TO EVENTUALLY MAKE THIS ACCURATE TO ACTUAL LOAN REPAYMENT
        RIGHT NOW IT'S A FLAT 10 YEAR LOAN WITH 0 INTEREST
        '''
        print "applying for loan (FAFSA standard)"
        rate = 0.039
        print "current student loan rate: {}".format(rate*100)


        pDate = self.week + self.validD['weeks2complete']
        periods = 20
        self.current_character.studentDebt = self.current_character.studentDebt + amount

        self.current_character.studentDebtRate = ((self.current_character.studentDebt)/ 120.0) # (Student Debt Amount / 120 Months)


    def weekly_event(self):
        print "weekly event!"
        if self.week % 4 == 0:
            self.monthly_event()
        return True

    def monthly_event(self):
        print "monthy event!"
        
        rent = 425.00
        print "your rent is due, {0}! (${1})".format(self.current_character.name, rent)

        if self.current_character.studentDebt > 0:
            print "your student loan payment is due, ${0}".format(round(self.current_character.studentDebtRate, 2))
            self.current_character.savings = self.current_character.savings - self.current_character.studentDebtRate

        self.current_character.savings = self.current_character.savings - rent
        return True


    def build_classifieds(self):
        print '-----building classfieds'
        jobsFile = helpers.get_relative_file('saves', 'locs1.fll')

        with open(jobsFile) as json_file:
            #simplejson.loads('json_file')
            self.classifieds = json.load(json_file)

    def displayTime(self):
        print "you have {} hours left".format(12 - self.timer)
        return True

    def c(self):
        exec(raw_input('enter raw command: '))
        return True



class Character():
    def __init__(   self,
                    name = None,
                    apartment = None,
                    hungry = False,
                    appearance = 0,
                    job = None,
                    salary = 0.00,
                    savings = 0.00,
                    education = 0,
                    speedMultiplier = 1,
                    workWeek = 12):

        self.name = None
        self.job = None 
        self.salary = 0
        self.savings = 0
        self.education = 0
        self.student = None
        self.studentDebt = 0
        self.studentDebtInit = 0
        self.studytime = 0

        self.attrList = [   self.name,
                            self.job,
                            self.salary,
                            self.savings,
                            self.education,
                            self.studentDebt,
                            self.student,
                            self.studytime]

        self.house = apartment
        self.hungry = hungry
        self.appearance = appearance
        self.speed = 14.28
        self.workWeek = 12#workWeek


    def save(self):
        charData = {}

        charData['name'] = self.name
        charData['job'] = self.job
        charData['savings'] = self.savings
        charData['salary'] = self.salary
        charData['education'] = self.education
        charData['studentDebt'] = self.studentDebt
        charData['studentDebtRate'] = self.studentDebtRate
        charData['student'] = self.student
        charData['studytime'] = self.studytime


        return charData

    def load(self, data):
        self.name = helpers.load_attr(data, 'name')
        self.job = helpers.load_attr(data, 'job')
        self.savings = helpers.load_attr(data, 'savings')
        self.salary = helpers.load_attr(data, 'salary')
        self.education = helpers.load_attr(data, 'education')

        student = helpers.load_attr(data, 'student')
        self.student = (student if student else 0)

        studentDebt = helpers.load_attr(data, 'studentDebt')
        self.studentDebt = (studentDebt if studentDebt else 0)

        studentDebtRate = helpers.load_attr(data, 'studentDebtRate')
        self.studentDebtRate = (studentDebtRate if studentDebtRate else 0)

        studytime = helpers.load_attr(data, 'studytime')
        self.studytime = (studytime if studytime else 0)       

        '''
        NEED TO MAKE THIS LOAD DYNAMIC FROM THE ATTRLIST Attribute
        if helpers.load_attr(data, 'studentDebt'):
            self.studentDebt = helpers.load_attr(data, 'studentDebt')

        '''
        return