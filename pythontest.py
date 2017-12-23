######################################
#                                    #
# Solution To Classic Chinese Puzzle #
#                                    #
######################################


def RabbitsAndChickens(heads, legs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if 2 * chickens + rabbits * 4 == legs:
            return [chickens, rabbits]
    return [None, None]


####################################
#                                  #
# Solution To Even Indexes Problem #
#                                  #
####################################


def EvenIndexes(s):
    data = s[::2]
    return "".join(data)


#######################################
#                                     #
# Solution To String Reversal Problem #
#                                     #
#######################################


def ReverseOrderString(s):
    data = s[::-1]
    return "".join(data)


##########################################
#                                        #
# Solution To Alphabets Counting Problem #
#                                        #
#####################################$$$$#


def CharacterCount(s):
    d = {}
    for c in s:
        if d.get(c) == None:
            d[c] = 1
        else:
            d[c] += 1

    return d

##########################################
#                                        #
# Solution To Method Overloading Problem #
#                                        #
##########################################

class Shape():
    def __init__(self):
        self.a = 0

    def area(self):
        self.a = 0
        return self.a

class Square(Shape):
    def __init__(self):
        super().__init__()

    def area(self):
        self.a = 2
        return self.a


##########################################
#                                        #
# Solution To Exception handling Problem #
#                                        #
##########################################


def ExceptionHandling():
    try:
        solution = 5/0
    except ZeroDivisionError as err:
        print(err)
    else:
        print(solution)


#############################################
#                                           #
# Solution To User And Company Name Problem #
#                                           #
#############################################


def UsernameAndCompanySeparator(s):
    uac = s.split('@')
    name, cname = "".join([x for x in uac[0] if x.isalpha()]), "".join([x for x in uac[1].rsplit('.', 1)[0] if x.isalpha()])
    return [name, cname]

############################################
#                                          #
# Solution To Words Of Only Digits Problem #
#                                          #
############################################


def WordsOfDigitsOnly(s):
    words = [x for x in s.split(" ") if x.isdigit()]
    return words


#######################################
#                                     #
# Solution To Sum Of Sequence problem #
#                                     #
#######################################


def SumOfSequence(n):
    res = 0
    for i in range(1, n+1):
        num = i / (i+1)
        res = res + num
    return round(res, 2)

print(SumOfSequence(5))