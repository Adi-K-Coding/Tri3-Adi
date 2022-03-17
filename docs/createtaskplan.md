{% include navigation.html %}

Description:
We have a class, with objects as trivia, and the attributes are questions, answers, and point values. A user is prompted with a question of how many questions they want, and then on input, loads one question with an input box to give the correct answer. A point count is kept, and correct answers add to the total. 

Outline:
Class has Trivia(Question, Answer, Point Value)

Check answer function
checkanswer =
if guess is equal to the answer, 
return true 
else false

score is set to 0
score = 0

objects are made using the attributes from the class
q1 = (question, answer, integer points)
q2 =("", "", #)
...

list is made using the objects
newlist = [q1, q2, ... ]

Function is created to take inputs and print responses based on correct or incorrect and the updated score
if run main
input = input("How many questions do you want)
take a random question in the list 
randomvalue =(for i in range int(input)...)
guess = input(randomvalue)

then use the check answer function given the guess as a parameter
if randomvalue.checkanswer(guess)
-update score
-print score
-print correct
else 
- print incorrect 
- print correct answer

finally remove that question as a possible question to come again



Requirements:
- [x] takes user input
- [x] uses a list
- [x] has a procedure with parameters
- [x] algorithm within procedure
- [x] calls to the procedure
- [x] instructions to use it

