def venueData():
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
    
'''
venues = venues()

for venue in venues.keys():
    print "___{}".format(venue)
    for job in venues[venue]['job']:
        print job
'''

