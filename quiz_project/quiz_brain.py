class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # def next_question(self):
    #     correct_question = self.question_list[self.question_number]
    #     answer = input(correct_question.text + " \"True\" or \"False\" answer: ")
    #     if correct_question.answer == answer:
    #         print("Your answer is correct.")
    #     else:
    #         print("Your answer is wrong.")
    #     self.question_number += 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is correct.")
            self.score += 1
        else:
            print("Your answer is wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)