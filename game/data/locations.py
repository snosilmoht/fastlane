'''
Add create venue function
custom maps storage
'''

class Location():
    def __init__(self, store_name, coordinates, jobs):
        self.store_name = store_name
        self.loc = coordinates

    def save(self):
        return

    def load(self):
        return

class Store(Location):
    def __init__(self, store_name, coordinates, jobs, shop):
        super(Location, self).__init__(store_name, coordinates, jobs)

        print self.store_name

class Jobs(self):
    def __init__(self):
        self.jobs = {}

    def add_job(self):
        title = raw_input('title: ')
        salary = raw_input('salary: ')
        prestige = raw_input('prestige: ')
        minApp = raw_input('minimum appearance 0-4: ')
        minEdu = raw_input('min education (0-4): ')

        self.jobs[title] = {'title': title,
                            'salary': salary,
                            'prestige': prestige,
                            'minApp': minApp,
                            'minEdu': minEdu}

    def save(self):
        jobData = {}

        #############################################


'''
venues = venues()

for venue in venues.keys():
    print "___{}".format(venue)
    for job in venues[venue]['job']:
        print job
'''

