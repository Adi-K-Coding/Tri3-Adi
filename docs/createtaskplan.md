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

