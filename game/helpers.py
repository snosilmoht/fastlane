import os

def get_functions(obj):
    lFns = [func for func in dir(obj) if callable(getattr(obj, func)) and not func.startswith("__")]
    return lFns

def input_integer(message = 'gimme integer'):

    badInput = True
    
    while badInput:
        try:
            out = int(input(message))
            badInput = False

        except ValueError:
            print 'please enter an integer.'

        except NameError:
            print 'please enter an integer.'


    return out

def interpreter(obj, keyword):
    '''
    builds dictionary to interpret simple commands into object methods
    returns appropriate function
    '''

    actionDict= {}
    method_list = get_functions(obj)

    for method in method_list:
        actionDict[method] = "obj.{}()".format(method)#obj.__dict__[method]

    act = [key for key in actionDict.keys() if key.lower() == keyword.lower()][0]
    exec(actionDict[act])

    return True

def get_relative_file(folderName = None, fileName = None):
    fileName = fileName

    relativePath = os.path.dirname(os.path.abspath(__file__))

    if folderName == '' or folderName == None:
        outFile = os.path.join(relativePath, fileName)

    else:
        fileDir = os.path.join(relativePath, folderName)
        outFile = os.path.join(fileDir, fileName)

    return outFile

def load_attr(source, key):
    try:
        'loading source'
        print '{0}: {1}'.format(key, source[key] )
        return source[key]

    except KeyError as e:
        print "{} missing from file, set to None".format(key)
        return None