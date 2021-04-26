'''The given function gives the sum of 2 nos. We used this function to test the pylint standards.'''
def add(number1, number2):
    '''This function returns addition of two nos'''
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))
