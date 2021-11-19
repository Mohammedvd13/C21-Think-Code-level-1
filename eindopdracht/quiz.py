print('Welkom bij Mohammed Shaikh zijn Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: Wat is je lievelingscodetaal?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Weet je hoe je Python gebruikt? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Vind je het leuk om te coderen?>')
    if answer.lower()=='':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('BEdankt voor je tijd om me quiz te spelen...',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')