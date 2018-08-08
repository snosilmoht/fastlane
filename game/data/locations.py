'''
Add create venue function
custom maps storage
'''


def locationData():
    venueDict = {

                'McDonalds' :
                                {
                                'job': 
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
                                    }
                                },
                                 
                'Bank' : 
                                {
                                'job': 
                                    {
                                    'Teller':
                                            {
                                             'title': 'Teller',
                                             'salary': 12,
                                             'prestige': 1,
                                             'minApp': 1,
                                             'minEdu': 1
                                            },
                                    'Supervisor':
                                            {
                                             'title': 'Supervisor',
                                             'salary': 14,
                                             'prestige': 2,
                                             'minApp': 1,
                                             'minEdu': 2
                                            },
                                    'Specialist':
                                            {
                                             'title': 'Specialist',
                                             'salary': 18,
                                             'prestige': 3,
                                             'minApp': 1,
                                             'minEdu': 3
                                            },
                                    'Broker':
                                            {
                                             'title': 'Broker',
                                             'salary': 25,
                                             'prestige': 5,
                                             'minApp': 2,
                                             'minEdu': 4
                                            }
                                    }
                                }
                }
    return venueDict



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

