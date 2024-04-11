import html


class Quiz:
    def __init__(self, question_list) -> None:
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        question_text = html.unescape(current_question.text)
        self.q_number += 1
        user_answer = input(f"\nQ.{self.q_number}: {question_text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.q_number}")
