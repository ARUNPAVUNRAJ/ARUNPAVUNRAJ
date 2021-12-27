print('Welcome to AskPython Quiz')
print('please use small letters for answers')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: who is the captain of indian national cricket team?')
    if answer.lower()=='virat kholi':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: what is the national bird of india? ')
    if answer.lower()=='peacock':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3:  which district is kallanai dam is located?')
    if answer.lower()=='tanjavur':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(') 
        
    answer=input('Question 4: Where is the Great Pyramid of Giza?')
    if answer.lower()=='egypt':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 5: who was the first american president?')
    if answer.lower()=='george washington':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
