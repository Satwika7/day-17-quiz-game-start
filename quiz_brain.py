from data import question_data
class Quiz:
    def __init__(self,question_list):
       self.question_number=0
       self.question_list = question_list
       self.score=0
    def still_has_questions(self):
        if self.question_number == len(question_data):
            return False
        else:
            return True

    def next_question(self):
        each_item = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {each_item.text} (True/False)?:")
        self.check_answer(each_item,user_answer)

    def check_answer(self,each_item,user_answer):
        if user_answer.title() == each_item.answer:
            self.score+= 1
            print(f"you are right,your current score is {self.score}/{self.question_number}")
        else:
            print(f"you are wrong,your current score is {self.score}/{self.question_number}")
        print("\n")

