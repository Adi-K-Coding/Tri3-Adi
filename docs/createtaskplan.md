{% include navigation.html %}


# Create Task
Link to Runtime Video: [Link](https://www.loom.com/share/829edf21b0a34f17b04e9d8413a11698)

Requirements:
- [x] takes user input
- [x] uses a list
- [x] has a procedure with parameters
- [x] algorithm within procedure
- [x] calls to the procedure
- [x] instructions to use it


***
## Code with Comments
``` python
import random as rand
import tkinter
from tkinter import messagebox
from tkinter import *

top = tkinter.Tk()


class Trivia:
    def __init__(self, question, answer, aa1, aa2, aa3):
        self.question = question
        self.answer = answer
        self.aa1 = aa1
        self.aa2 = aa2
        self.aa3 = aa3

        # trivia class with constructor and attributes
        # aa1, aa2, aa3 stand for alternate answers 1, 2, and 3


score1 = 0  # score variable
# question bank of all the questions and the correct answers + alternate answers
question1 = Trivia("Who won the world series in 1988? ", "Dodgers", "Padres", "Yankees", "Red Sox")
question2 = Trivia("Who won superbowl 50? ", "Broncos", "Seahawks", "Patriots", "Panthers")
question3 = Trivia("Who is on the one dollar bill? ", "George Washington", "Thomas Jefferson", "Albert Einstein",
                   "Lewis Hamilton")
question4 = Trivia("What is the largest Ocean? ", "Pacific", "Atlantic", "Indian", "Arctic")
question5 = Trivia("What is the square root of 49? ", "7", "4.9", "6", "49")
question6 = Trivia("Which of these was not an Axis Power during WWII? ", "France", "Germany", "Italy", "Japan")
question7 = Trivia("How many stripes does the US flag have? ", "13", "12", "14", "50")
question8 = Trivia("What is a group of lions called? ", "A pride", "A murder ", "A herd", "A flock")
question9 = Trivia("What US state has the largest area? ", "Alaska", "Texas", "California", "Florida")
question10 = Trivia("What movie was the song \"Life is a Highway\" In? ", "Cars", "Toy Story", "Moana", "Star Wars")
question11 = Trivia("What does OOP stand for in computer science? ", "Object Oriented Programming",
                    "One Orange Penguin", "Out of Packets", "Orcas Orchestrate Politics")
question12 = Trivia("The olympics are held every how many years? ", "4", "2",
                    "200", "1")
question13 = Trivia("In American Football, six points are scored for a what? ", "Touchdown", "Field Goal", "Safety",
                    "Tackle")
question14 = Trivia("What sport is referred to as \"America's pastime\"? ", "Baseball",
                    "Tennis", "Football", "Soccer")
question15 = Trivia("Who was the first man on the moon? ", "Neil Armstrong", "Donald Trump", "Buzz Aldrin", "Elon Musk")

# all questions getting added to a list of questions called questionList
questionList = [
    question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,
    question11, question12, question13, question14, question15
]


def create_question():
    random_value = questionList[
        rand.randint(0, len(questionList) - 1)]  # selects random question from list of questions
    answer_list = [random_value.aa1, random_value.aa2, random_value.aa3, random_value.answer]  # stores the correct
    # answer plus the three alternate answers so their order can be shuffled on the next line
    rand.shuffle(answer_list)  # shuffles answers so that the correct answer does not appear on the top everytime
    # the four buttons are being created, with each button having an answer, one button has the correct answer and the
    # three other buttons have the incorrect alternate answer. Everytime a button is clicked, it calls the check answer
    # function below with that buttons value and the random question that was generated so that the button's value can
    # be checked to see if it is right or wrong
    b1 = tkinter.Button(top, text=answer_list[0], command=lambda: check_answer(answer_list[0], random_value))
    b2 = tkinter.Button(top, text=answer_list[1], command=lambda: check_answer(answer_list[1], random_value))
    b3 = tkinter.Button(top, text=answer_list[2], command=lambda: check_answer(answer_list[2], random_value))
    b4 = tkinter.Button(top, text=answer_list[3], command=lambda: check_answer(answer_list[3], random_value))

    # setting the text of the question to be displayed, as well at the text for the score variable
    text = tkinter.StringVar()
    text.set(random_value.question)
    label = tkinter.Label(top, textvariable=text, relief=FLAT)
    label.pack()
    score_label = tkinter.StringVar()
    score_label.set("Score: " + str(score1))
    label1 = tkinter.Label(top, textvariable=score_label, relief=FLAT)
    label1.pack()
    b1.pack(fill=X)
    b2.pack(fill=X)
    b3.pack(fill=X)
    b4.pack(fill=X)
    top.mainloop()


def check_answer(user_answer, rv):
    global score1
    # checks if the passed in value of the button that was clicked(user_answer) is equal to the correct answer to the
    # random question(rv)
    if user_answer == rv.answer:
        # if correct, score increases by 1 and it displays correct
        score1 = score1 + 1
        messagebox.showinfo("", "Correct")
    else:
        # if incorrect, score doesn't change and it displays the correct answer
        messagebox.showinfo("", f"Incorrect, the correct answer was {rv.answer}")
    # the question is then removed from the list of questions so that it doesn't appear again
    questionList.remove(rv)
    #  gets rid of the current question that is being displayed so that the next question can be displayed
    top.quit()
    for widget in top.winfo_children():
        widget.destroy()


if __name__ == "__main__":
    userquestions = 15
    # for loop to call function that makes the questions pop up on the screen
    for i in range(userquestions):
        create_question()
    messagebox.showinfo("End Screen", f"Great Job, your total score was: {score1}")

```

***


# Write Up: 
# 3
## 3a. Provide a written response that does all three of the following
### I. Describes the overall purpose of the program
The overall purpose of the program is to quiz users on trivia questions. There is a bank of questions(currently 15 questions but the way that the program is created makes it extremely easy to add questions). When the user selects an answer by clicking a button(input), the program tells them if they got the answer correct or not(output), and if they got it wrong, it tells them the correct answer. It also has a running tracker of the user's score to keep track of how many questions the user has answered correctly.
### II. Describes what functionality of the program is demonstrated in the video
In the video, I answer questions, and I get some right and get others wrong to demonstrate what happens when a user enters correct vs incorrect answers. 
### III. Describes the input and output of the program demonstrated in the video
When you select an answer from the four buttons(input), it will display “correct” and increase your score by one, however, when you enter an incorrect input/answer to the question, it will display an “incorrect”, and will tell you the correct answer. Score doesn't change if you get an answer incorrect. 

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.
### I. The first program code segment must show how data has been stored in the list
``` python
question1 = Trivia("Who won the world series in 1988? ", "Dodgers", "Padres", "Yankees", "Red Sox")
question2 = Trivia("Who won superbowl 50? ", "Broncos", "Seahawks", "Patriots", "Panthers")
question3 = Trivia("Who is on the one dollar bill? ", "George Washington", "Thomas Jefferson", "Albert Einstein", "Lewis Hamilton")
...
question15 = Trivia("Who was the first man on the moon? ", "Neil Armstrong", "Donald Trump", "Buzz Aldrin", "Elon Musk")


questionList = [
    question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,
    question11,question12, question13, question14, question15
]

```
### II. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose 
``` python
random_value = questionList[rand.randint(0, len(questionList) - 1)]

text = tkinter.StringVar()
    text.set(random_value.question) # setting the text of the question to be displayed using the random_value variable
    label = tkinter.Label(top, textvariable=text, relief=FLAT)

```
## THEN PROVIDE A WRITTEN RESPONSE THAT DOES ALL THREE OF THE FOLLOWING
### III, Identifies the name of the list being used in this response
The name of the list is called questionList, as it is a list of questions

### IV. Describes what the data contained in the list represent in your program
The data containted in the list represents the different questions that can be asked to the user, in question I, we see the questions(question1, question2...) being created, which each question getting a question, the correct answer, and three alternate answers, and then we see the questions getting added to questionList. 

### V. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
If I didn't use the list, the program would have been much more different because I would have had to manually display/hard code every question and there would have been much more code that I would have to make. By making a list, we can save a lot of time and code by just using the list and iterating through it. 

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure

### I. The first program code segment must be a student-developed procedure that:
### Defines the procedure’s name and return type (if necessary)
### Contains and uses one or more parameters that have an effect on the functionality of the procedure
### Implements an algorithm that includes sequencing, selection, and iteration 
``` python
def check_answer(user_answer, rand_val):
    global score1
    # checks if the passed in value of the button that was clicked(user_answer) is equal to the correct answer to the
    # random question(rv)
    if user_answer == rand_val.answer:
        # if correct, score increases by 1 and it displays correct
        score1 = score1 + 1
        messagebox.showinfo("", "Correct")
    else:
        # if incorrect, score doesn't change and it displays the correct answer
        messagebox.showinfo("", f"Incorrect, the correct answer was {rv.answer}")
    # the question is then removed from the list of questions so that it doesn't appear again
    questionList.remove(rand_val)
    #  gets rid of the current question that is being displayed so that the next question can be displayed
    top.quit()
    for widget in top.winfo_children():
        widget.destroy()
```


### The second program code segment must show where yourstudent-developed procedure is being called in your program.
``` python
    random_value = questionList[rand.randint(0, len(questionList) - 1)]  # selects random question from list of questions
    answer_list = [random_value.aa1, random_value.aa2, random_value.aa3, random_value.answer]  # stores the correct
    # answer plus the three alternate answers so their order can be shuffled on the next line
    rand.shuffle(answer_list)  # shuffles answers so that the correct answer does not appear on the top everytime
    # the four buttons are being created, with each button having an answer, one button has the correct answer and the
    # three other buttons have the incorrect alternate answer. Everytime a button is clicked, it calls the check answer
    # function with that buttons value and the random question that was generated so that the button's value can
    # be checked to see if it is right or wrong
    b1 = tkinter.Button(top, text=answer_list[0], command=lambda: check_answer(answer_list[0], random_value))
    b2 = tkinter.Button(top, text=answer_list[1], command=lambda: check_answer(answer_list[1], random_value))
    b3 = tkinter.Button(top, text=answer_list[2], command=lambda: check_answer(answer_list[2], random_value))
    b4 = tkinter.Button(top, text=answer_list[3], command=lambda: check_answer(answer_list[3], random_value))

```

##THEN PROVIDE A WRITTEN RESPONSE THAT DOES BOTH OF THE FOLLOWING:

### III. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The procedure identified is the function which is called whenever the user enters an input(clicks the button with the answer they select). When the user clicks their enter the check_answer method is called, and this contributes to the overall functionality of the program because it is what creates the output for the user. In other words, the method call is the way the user's input interacts with the program, and how the output is displayed to the user. It let's them know if the input they entered was correct or not. 

### IV. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it
Everytime they click on the button with the answer they select, it calls the check_answer function with the value of the button they selected, as well as the passed in random_value variabel. The function then checks if the value they selected corresponds with the answer value for the random_value that was passed in. If it matches, it displays "correct" and increases the score by one. If it doesn't match, it displays "incorrect" and the correct answer. 

## 3d. Provide a written response that does all three of the following:

### I. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. 
### First call: 
Example call is the question asking: "Who is on the one dollar bill?" and the user clicks on the button with "George Washington", which then calls the check_answer method with the parameters (users answer which in this case is George Washington, and random value that was generated that correponds to that question)
### Second call: 
Example call is the question asking: "Who was the first man on the moon?" and the user clicks on the button with "Elon Musk", which then calls the check_answer method with the parameters (users answer which in this case is Elon Musk, and random value that was generated that correponds to that question)

### II. Describes what condition(s) is being tested by each call to the procedure
### Condition(s) tested by the first call: 
In the first call, the method tests if the user input in this case "George Washington" is correct for the question "Who is on the one dollar bill?". An if statement is used to make the comparison, and test if the user's input "George Washington" matches the answer for the question passed in(rand_val), and the result of the call is displayed below.
### Condition(s) tested by the second call:
In the first call, the method tests if the user input in this case "Elon Musk" is correct for the question "Who was the first man on the moon?". An if statement is used to make the comparison, and test if the user's input "Elon musk" matches the answer for the question passed in(rand_val), and the result of the call is displayed below.

### III. Identifies the result of each call
### Result of the first call: 
In call 1, the if statement is true, the user input is correct, so the message will pop up "Correct" and the score increases by one. 
### Result of the second call: 
In call 2, the if statement is false, and user input is not correct, so the message will pop up "Incorrect, the correct answer was Neil Armstrong" and the score stays the same.

# Planning
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

