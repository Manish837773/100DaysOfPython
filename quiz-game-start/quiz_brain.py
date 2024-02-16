class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        question_asked = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {question_asked.question} True/False: ").lower()
        return user_answer

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def scoring(self):
        answer = self.question_bank[self.question_number].answer
        if self.next_question().lower() == answer.lower():
            print("You've got it right!\nYou get 1 point")
            self.score += 1
            print(f"You're score is {self.score}/12\n")
        else:
            print("Sorry this is wrong\n")

    def printter(self, question, last):
        print(question)
        self.score += 1
        