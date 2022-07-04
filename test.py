print('Welcome to my quiz, answer the questions')
playing = input('Do you want to play? (yes/no)')

if playing != 'yes':
        quit()
print('Ok, lets play. ')
score = 0

answer = input('How old am I? ')
if answer == '24':
    print('Thats right')
    score += 1
else:
    print("You're wrong")

answer = input('What is the name of company that I work for? ')
if answer == 'Billennium':
    print('Thats right')
    score += 1
else:
    print("You're wrong")

answer = input('What is my dogs name? ')
if answer == 'Mania':
    print('Thats right')
    score += 1
else:
    print("You're wrong")

answer = input('What is my gf name? ')
if answer == 'Klaudia':
    print('Thats right')
    score += 1
else:
    print("You're wrong")

answer = input('What is my role in Billennium? ')
if answer == 'Support':
    print('Thats right')
    score += 1
else:
    print("You're wrong")

percentage = score / 5 * 100
print('Your score is ' + str(percentage) + '%.')