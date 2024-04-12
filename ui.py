from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_lb = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lb.grid(row=0, column=1)

        # canvas
        self.canvas = Canvas(width=300, height=300)
        self.text = self.canvas.create_text(150, 150, width=280, font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, border=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, border=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_lb.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question_text)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")

    def answer_true(self):
        self.feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
