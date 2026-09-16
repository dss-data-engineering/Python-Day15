from data import question_data


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def still_has_questions(self):
        if self.question_number+1 <= len(self.questions):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("That\'s correct!")
            self.score += 1
        else:
            print("That\'s wrong.")
        print("The correct answer was: " + correct_answer)
        print(f"Score:{self.score}/{self.question_number + 1}")
        print("\n")

    def next_question(self):
        candidate_answer = input(f"Q.{self.question_number + 1} {self.questions[self.question_number].question} (True/False)?\n").lower()
        self.check_answer(candidate_answer, self.questions[self.question_number].answer)
        self.question_number += 1

