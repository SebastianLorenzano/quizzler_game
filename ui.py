from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window #
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Canvas #
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Some Question Things",
                                                   font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Labels #
        self.score_label = Label(text="Score: 0/0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=1)
        # Buttons #
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(width=85, height=85, image=true_image, highlightbackground=THEME_COLOR,
                                  command=self.true_button)
        self.false_button = Button(width=85, height=85, image=false_image, highlightbackground=THEME_COLOR,
                                   command=self.false_button)
        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="GAME OVER")
            print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

    def true_button(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(players_decision="True")
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.is_right_highlight()
            self.window.after(1000, func=self.color_back)
            self.get_next_question()

    def false_button(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer(players_decision="False")
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.is_right_highlight()
            self.window.after(1000, func=self.color_back)
            self.get_next_question()

    def color_back(self):
        self.canvas.config(bg="white")

    def is_right_highlight(self):
        if self.quiz.is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.color_back)
