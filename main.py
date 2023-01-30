from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# globals
question_bank = []

# data
for key in question_data:
    text = key["question"]
    answer = key["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

# Game
quiz = QuizBrain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print("You've completed de quiz")
print(f"you current score was {quiz.score}/{quiz.question_number}")
