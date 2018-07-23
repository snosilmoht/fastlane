myList = {'a': 'ehh', 'ASDF': "bee", 'c': "see"}

myListLower = [key.lower() for key in myList.keys()]
print myListLower

if 'asdf'.lower() in myListLower:
    print 'true'