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

    # setting the text of the question to be displayed using the random value variable, as well at the text for the
    # score variable
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


def check_answer(user_answer, rand_val):
    # collaborated with Rohan Gaikwad for the idea of the check answer method
    global score1
    # checks if the passed in value of the button that was clicked(user_answer) is equal to the correct answer to the
    # random question(rand_val)
    if user_answer == rand_val.answer:
        # if correct, score increases by 1 and it displays correct
        score1 = score1 + 1
        messagebox.showinfo("", "Correct")
    else:
        # if incorrect, score doesn't change and it displays the correct answer
        messagebox.showinfo("", f"Incorrect, the correct answer was {rand_val.answer}")
    # the question is then removed from the list of questions so that it doesn't appear again
    questionList.remove(rand_val)
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
