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


#  Student Loan Interest
def interestCalc(principle, rate, time):
    '''
    A = P * ((1 + (r/n)) ^ n*t)
    A = amount
    P = principle
    r = interest rate
    t = total number years
    n = number compounding per year
    ARGS:
        Principal Amount
        Rate of Interest per year as a percent
        Time Period involved in MONTHS
        (student loans comound daily)

    RETURN:
        interest:   accrued interest
    '''

    P = float(principle)
    r = float(rate)
    t = float((time/12))
    n = 365.00

    A = P * ((1 + (r/n)) ** (n*t))

    return A






def loanPmt(principle, rate, periods):
    Pv = float(principle)
    R = float(rate)#.01 * rate
    print "rate: {}".format(R)
    Pr = float(periods)

    amt = float((Pv * R)/(1-(1 + R)**(-1*Pr)))
    amt = round(amt, 2)

    return amt

#  FAFSA Loan Options
#  https://studentaid.ed.gov/sa/repay-loans/understand/plans


def fafsaStandard(principle, rate):
    '''
    This repayment plan saves you money over time because
    your monthly payments may be slightly higher than payments
    made under other plans, but you will pay off your loan
    in the shortest time. For this reason, you will pay
    the least amount of interest over the life of your loan.

    based on principle loan amount:
    at least        less than       repayment period:
    $0              $7,500          10 years
    $7501           $10,000         12 years
    $10,001         $20,000         15 years
    $20,001         $40,000         20 years
    $40,001         $60,000         25 years
    $60,001                         30 years
    '''

    Pv = principle

    if Pv < 7501:
        Pr = 10

    elif Pv < 10001:
        Pr = 12

    elif Pv < 20001:
        Pr = 15

    elif Pv < 40001:
        Pr = 20

    elif Pv > 60000:
        Pr = 30

    interest = loanPmt(Pv, rate, Pr)
    interest = round(interest, 2)

    return interest

Pv = 26946
i = 0.039
Pr = 72

print interestCalc(Pv, i, Pr)