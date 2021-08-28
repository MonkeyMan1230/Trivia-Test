print('Hello, Welcome to Brians Trivia Quiz!')
print('Try your best at answering!')

totalquestions = 3
score = 0

ans = input('Are you ready Yes/No?')

if ans.lower() == 'yes':

    ans = input('1. Is my favorite color red?')

    if ans.lower() == 'yes':
      print('Correct!')
      score += 1
    else:
        print('Incorrect')

    ans = input('2. What is 8 x 8 + 4=')

    if ans.lower() == '68':
      print('Correct!')
      score += 1
    else:
        print('Incorrect')

    ans = input('3. Say yes for free points!!!')

    if ans.lower() == 'yes':
      print('Correct!')
      score += 1
    else:
        print('Incorrect')

print('You got', score, "Questions Correct.")
mark = (score/totalquestions) * 100

print("Mark:", mark)
print('Thanks For Playing, Good Bye!!!!')
