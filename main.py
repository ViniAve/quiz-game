from question_model import Question
from quiz_brain import Quiz
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

question = Quiz(question_bank)

while question.still_has_question():
    question.next_question()

print("\nYou've completed the quiz!")
print(f"Your final score is {question.score}/{question.q_number}")
