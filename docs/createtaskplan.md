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
question6 = Trivia("What's the capital of Chile? ", "Santiago", "Washington D.C.", "Paris", "Madrid")
question7 = Trivia("What is the capital of France? ", "Paris", "Munich", "Amsterdam", "Moscow")
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


Write Up: 
# 3
## 3a. Provide a written response that does all three of the following
### I. Describes the overall purpose of the program
The overall purpose of the program is to quiz users on trivia questions. There is a bank of questions(currently 15 questions but the way that the program is created makes it extremely easy to add questions). When the user inputs an answer the program tells them if they got the answer correct or not, and if they got it wrong, it tells them the correct answer. It also has a running tracker of the user's score to keep track of how many questions the user has answered correctly.
### II. Describes what functionality of the program is demonstrated in the video
In the video, I answer questions, and I get some right and get others wrong to demonstrate what happens when a user enters correct vs incorrect answers. 
### III. Describes the input and output of the program demonstrated in the video
When you enter a correct input to the prompt, it will display “correct” and increase your score by one, however, when you enter an incorrect input to the question, it will display an “incorrect”, and will tell you the correct answer

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program.
### I. The first program code segment must show how data has been stored in the list
question1 = Trivia("Who won the world series in 1988 ", "Dodgers")
question2 = Trivia("Who won superbowl 50 ", "Broncos")

questionList = [
    question1, question2, question3, question4, question5, question6, question7, question8, question9, question10,
    question11,question12, question13, question14, question15
]

### II. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose 
random_value1 = questionList[rand.randint(0, len(questionList) - 1)]

return render_template("createtask.html", randomvalue=random_value1, score1=score1, display=display)

(On Front End-question being displayed): `<h2 style="color:midnightblue">{{ randomvalue.question }}</h2>`

## THEN PROVIDE A WRITTEN RESPONSE THAT DOES ALL THREE OF THE FOLLOWING
### III, Identifies the name of the list being used in this response
The name of the list is called questionList, as it is a list of questions

### IV. Describes what the data contained in the list represent in your program
The data containted in the list represents the different questions that can be asked to the user, in question I, we see question1 and question 2 being created, which each question getting a question, and answer, and then we see the questionList adding all the different questions to itself

### V. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list
If I didn't use the list, the program would have been much more different because I would have had to manually display/hard code every question and there would have been much more code that I would have to make. By making a list, we can save a lot of time and code by just using the list and iterating through it. 

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure

### I. The first program code segment must be a student-developed procedure that:
### Defines the procedure’s name and return type (if necessary)
### Contains and uses one or more parameters that have an effect on the functionality of the procedure
### Implements an algorithm that includes sequencing, selection, and iteration 
```def createtask():```
    ```global score1```
    ```global display```
    ```global state```
    ```display = " "```
    ```h = request.args.get('answer', '')```
    ```userinput = request.form.get('userinput')```

    if state:
        display = " "
    else:
        if userinput == h:
            score1 = score1 + 1
            print("it works")
            print(score1)
            display = "Correct!"
        else:
            # questionList.remove(random_value1)
            print("it doesnt work")
            display = "Incorrect, the correct answer was: " + h

    random_value1 = questionList[rand.randint(0, len(questionList) - 1)]
    state = False
    return render_template("createtask.html", randomvalue=random_value1, score1=score1, display=display)


### The second program code segment must show where yourstudent-developed procedure is being called in your program.

`<form action="/ct/createtask/?answer={{ randomvalue.answer }}" method="POST" class="form" style = "position: relative; text-align: center;">`
        `<h2 style="color:midnightblue">{{ randomvalue.question }}</h2>`
        `<input type="text" placeholder="Enter Your Answer" name='userinput'>`
        `<button type="submit">Submit</button>`
    `</form>`

##THEN PROVIDE A WRITTEN RESPONSE THAT DOES BOTH OF THE FOLLOWING:

### III. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The procedure identified is the python side of my project which takes the user input from the front end(which is the html side) when the user clicks submit, checks if the user's answer is correct in the backend(python), and accordingly returns an output on the front end which tells them if their answer was correct or not, and if it was incorrect, displays the correct answer. Their score is also updated accordingly. 

### IV. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it
First the front end takes a random question from the list and displays it, then the user enters an answer, and it is sent to the python, where it is checked to see if the answer was correct or not. If the answer was correct, it will tell the front end to display correct and this shows the user that the input they entered was correct and increase the score by one. However, if the answer the user entered was incorrect, the frontend will display "incorrect", followed by the correct answer, and the score will not change. Everytime the submit is clicked, the question changes, and the if statement is checked to see if the answer was correct or not. 

## 3d. Provide a written response that does all three of the following:

### I. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. 
### First call: 
Example call is the question asking: "Who won the world series in 1988" and the user answers "Dodgers", and clicks the submit button, which would make a call to the backend
### Second call: 
Example call is the question asking: "Who won superbowl 50 " and the user answers "asdf", and clicks the submit button, which would make a call to the backend

### II. Describes what condition(s) is being tested by each call to the procedure
### Condition(s) tested by the first call: 
In the first call, the python tests if the user input in this case "Dodgers" is correct for the question "Who won the world series in 1988". An if statement is used to make the comparison, and the result of the call is displayed below.
### Condition(s) tested by the second call:
In the second call, the python tests if the user input in this case "asdf" is correct for the question "Who won Superbowl 50". An if statement is used to make the comparison, and the result of the call is displayed below.

### III. Identifies the result of each call
### Result of the first call: 
In call 1, the if statement is true, the user input is correct, so on the front end it displays "Correct" and the score increases by one. 
### Result of the second call: 
In call 2, the if statement is false, and user input is not correct, so on the front end it displays "Incorrect, the correct answer was Broncos" and the score stays the same.

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

