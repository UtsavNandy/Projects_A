class QuizBrain :
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list =q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    
         

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        useranswer = input(f"Q.{self.question_number}{current_question.text}(True/False):")
        self.check_answer(useranswer, current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() ==  correct_answer.lower():
            print("Correct")
            self.score =self.score + 1
        else:
            print(f"Sorry, that's wrong. The correct answer is {correct_answer}")
        print(f"Your current score is :{self.score}|{self.question_number}")
