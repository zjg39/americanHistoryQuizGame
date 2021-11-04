# Quiz Game Project
import time

print('Welcome to the Quiz!')

readyornot = input('Are you ready to play?  ').lower()

if readyornot.lower() != 'yes':
    print('Okay, we\'ll see you next time!')
    quit()
else:
    print('Okay, let\'s play a game!')
time.sleep(2)

score = 0
answer1 = input('How many stripes does the American flag have?  ').lower()
if answer1 != 'thirteen':
    print('Ooo, sorry! That answer is incorrect. There are thirteen stripes on the American flag.')
    score = score - 1
else:
    print('That is correct! Good job!')
    score = score + 1



time.sleep(2)
answer2 = input('Which Founding Father is pictured on the $100 bill?  ').lower()
if answer2 != 'benjamin franklin':
    print('That is incorrect. The man on the $100 bill is Benjamin Franklin!')
    score = score - 1
else:
    print('That is correct! Good job!')
    score = score + 1



time.sleep(2)
answer3 = input('What is the biggest state in the United States?  ').lower()
if answer3 != 'alaska':
    print('Nope! The largest state in the union is Alaska!')
    score = score - 1
else:
    print('Right! Alaska has an area of over 586,000 square miles!')
    score = score + 1



time.sleep(2)
answer4 = input('Who served as the first president of the United States?  ').lower()
if answer4 != "george washington":
    print('Aaaahh, sorry!  The correct answer is \'George Washington\'.')
    score = score - 1
else:
    print('That\'s correct! George Washington was the first American president!')
    score = score + 1



time.sleep(2)
if score > 2:
    print('You\'re doing great! Keep going!')
elif score <= 2:
    print('Your history needs some work!')


time.sleep(2)
answer5 = input('When did the American Revolutionary War begin?  ')
if answer5 != '1775':
    print('That is not correct. The American Revolutionary War began in 1775!')
    score = score - 1
else:
    print('That is correct! Great job!')
    score = score + 1


time.sleep(2)
answer6 = input('Who assassinated president Abraham Lincoln?  ').lower()
if answer6 != 'john wilkes booth':
    print('Nope! John Wilkes Booth shot president Lincoln at the Ford Theatre in 1865.')
    score = score - 1
else:
    print('That\'s right! You know your history!')
    score = score + 1


time.sleep(2)
answer7 = input('In what year did Hawaii become a state in the United States?  ')
if answer7 != '1959':
    print('That\'s not right. Hawaii became a state in 1959.')
    score = score - 1
else:
    print('That is correct!')
    score = score + 1


time.sleep(1)
print('Let\'s see how you did! Let\'s calculate your score...')
time.sleep(.5)
print('Calculating...')
time.sleep(2)

print('Your final score was ' + str(score)+'!')
time.sleep(1)

if score == 7:
    print('WOW! You know your stuff!  Congratulations!')
elif score < 7 and score > 3:
    print('Not perfect, but pretty good!  Keep studying!')
else:
    print('Time to hit the books!')