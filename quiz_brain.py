import html


class QuizBrain:
    def __init__(self, question_list) -> None:
        self.q_number = 0
        self.q_list = question_list
        self.score = 0
        self.current_question = ""

    def still_has_question(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        self.current_question = self.q_list[self.q_number]
        question_text = html.unescape(self.current_question.text)
        self.q_number += 1
        return f"\nQ.{self.q_number}: {question_text}"

    def check_answer(self, user_answer):
        if user_answer == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False
