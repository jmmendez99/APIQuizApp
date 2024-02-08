from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question text.",
            font=FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # labels
        self.lbl_score = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(row=0, column=1)

        # buttons
        btn_true_img = PhotoImage(file="./images/true.png")
        self.btn_true = Button(
            image=btn_true_img,
            highlightthickness=0,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.true_pressed
        )
        self.btn_true.grid(row=2, column=0)
        btn_false_img = PhotoImage(file="./images/false.png")
        self.btn_false = Button(
            image=btn_false_img,
            highlightthickness=0,
            bd=0,
            activebackground=THEME_COLOR,
            command=self.false_pressed
        )
        self.btn_false.grid(row=2, column=1)

        # Call get_next_question to populate canvas with question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.lbl_score.config(text=f"Score:{self.quiz.score}", font=FONT)
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
