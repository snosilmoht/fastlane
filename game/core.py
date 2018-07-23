

class SimpleGame():
    def __init__(self, weekNb = 1, workWeek = 12):
        self.week = weekNb
        self.workWeek = workWeek
        self.timer = self.workWeek

        print "____new game"

        charName = raw_input("enter your name: ")

        self.curJobs = classifieds()

        self.player = Character(
                                name = charName,
                                time = self.workWeek,
                                currentJobs = self.curJobs,
                                speedMultiplier = .33
                                )

        self.actionDictionary()

        while self.week <= 3:
            self.curJobs = classifieds()
            self.player.classifieds = self.curJobs
            print "_____Week {} _____".format(self.week)
            self.player.timer = self.workWeek
            self.runWeek()

    def actionDictionary(self):
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
        while self.timer > 0:
            self.timer = self.player.timer
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

                if act.lower() not in [key for key in self.actionDict.keys()]:
                    print "improper command"

                else:
                    exec(self.actionDict[act])
                    print "timer left: {}".format(self.player.timer)
                    print "savings: {}".format(self.player.savings)
                    #print self.actionDict[act]
        if self.timer <= 0:
            self.week += 1
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
                    name = "joe",
                    currentJobs = None,
                    time = 12.0,
                    apartment = None,
                    hungry = False,
                    appearance = 0,
                    job = None,
                    salary = 0,
                    savings = 0,
                    education = 0,
                    speedMultiplier = 1):

        self.name = name
        self.classifieds = currentJobs
        self.timer = time
        self.house = apartment
        self.hungry = hungry
        self.appearance = appearance
        self.job = currentJobs.jobs['McDonalds']['Cook']#job
        self.speed = 1
        self.salary = salary
        self.savings = savings
        self.education = education


    def relax(self):
        '''
        generic action to just take up time
        '''
        print "timer reduced by {} hours".format(self.speed)
        self.timer = self.timer - self.speed
        self.showCounter()

    def showCounter(self):
        print 'you have {} hours left'.format(self.timer)

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
            self.timer = self.timer - (1*self.speed)
            if self.timer < 0:
                overage = float(1.0 - abs(self.timer))
                self.savings = self.savings + (self.savings * overage)
                #self.timer = 0

            self.savings = self.salary + self.savings
            



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
