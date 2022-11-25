from data import question_data
from question_model import Question
from quiz_brain import Quiz
question_bank = []
for each_question in question_data:
    question_bank.append(Question(each_question["text"], each_question["answer"]))
new_quiz = Quiz(question_bank)
while new_quiz.still_has_questions():
    new_quiz.next_question()
print("you've completed the quiz!")
print(f"your final score is {new_quiz.score}/{new_quiz.question_number}")