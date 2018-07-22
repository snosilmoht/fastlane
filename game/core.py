def test():
    print 'hello world!'

class SimpleGame():
    def __init__(self, weekNb = 0):
        self.week = weekNb

        print "____new game"

        myName = raw_input("enter your name: ")
        #print "Character Created, hi {}!".format(player1.name)

        self.curJobs = classifieds()

        self.player = Character(    name = myName,
                                currentJobs = self.curJobs,
                                speedMultiplier = .33)

        print '----------------'
        print self.player.name
        print '-----------------------------'

        while self.week < 2:
            self.curJobs = classifieds()
            self.player.classifieds = self.curJobs
            print "_____Week {} _____".format(self.week)

            self.Work()


    def Work(self):
        while self.player.timer > 0:
            act = input("enter command: ")
        self.week += 1

class classifieds():
    def __init__(self):
        self.null = None

        self.Jobs = {   'Cook':{'Title': 'Cook', 'salary': 10, 'prestige': 1, 'minApp' : 0},
                        'Supervisor': {'Title': 'Supervisor', 'salary': 12, 'prestige': 2, 'minApp' : 0},
                        'Manager': {'Title': 'Manager', 'salary': 15, 'prestige': 3, 'minApp' : 1},
                        'Owner': {'Title': 'Owner', 'salary': 25, 'prestige': 5, 'minApp' : 2}
                    }

    def listJobs(self):
        print "listing jobs"
        for key in self.Jobs.keys():
            print key #  , self.Jobs[key]

    def applyForJob(self, job = None, appearance = 0):
        if job == None:
            "please select a job"
            return None

        else:
            print "you selected {}".format(job)

            if appearance < self.Jobs[job]['minApp']:
                print "you did not get the job, need better appearance"
                return None
            else:
                print 'you got hired as {0}, with a salary of {1}'.format(job, self.Jobs[job]['salary'])
                return self.Jobs[job]


class Character():
    def __init__(   self,
                    name = "joe",
                    currentJobs = None,
                    time = 12.0,
                    apartment = None,
                    hungry = False,
                    appearance = 0,
                    job = None,
                    speedMultiplier = 1):

        self.name = name
        self.classifieds = currentJobs
        self.timer = time
        self.house = apartment
        self.hungry = hungry
        self.appearance = appearance
        self.job = job
        self.speed = 1
        print self.classifieds

    def relax(self):
        '''
        generic action to just take up time
        '''
        print "timer reduced by {} hours".format(self.speed)
        self.timer = self.timer - self.speed
        print 'you have {} hours left'.format(self.timer)

    def applyForJob(self): #jobName):
        print "applying"
        print self.classifieds.listJobs()
        jobApp = raw_input("what job do you want to apply for? ")


        self.job = self.classifieds.applyForJob(jobApp, self.appearance)

        if self.job:
            print "you are now {}".format(self.job)

        self.timer = self.timer - .25

    def work(self):
        print "working"


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
