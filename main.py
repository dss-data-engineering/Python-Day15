from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main():
    question_bank = []

    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("Thank you for completing the quiz!\n")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


main()