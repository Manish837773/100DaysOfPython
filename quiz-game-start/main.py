import data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

data = data.question_data

for text in data:
    question_map = text
    question = question_map["text"]
    answer = question_map["answer"]
    question_obj = Question(question, answer)
    question_bank.append(question_obj)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.scoring()

print("You've completed the quiz!")
print(f"You're final score is {quiz_brain.score}/12")