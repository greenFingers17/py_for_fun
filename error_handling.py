print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats!')
    elif int(numCats) < 0:
        raise NameError('The number of cats cannot be a negative value.')
    elif int(numCats) == 0:
        print('Seems like you do not have any cats at all!')
    else:
        print('That is not many.')
except ValueError:
    print('Please make sure to enter a number.')

