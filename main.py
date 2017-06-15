import pyexcel as pe
import pyexcel_xlsx
import random

class question:
    def __init__(self,number,type,difficulty,q,ans,option1,option2,option3,option4):
        self.q_number = number
        self.q_type = type
        self.q_difficulty = difficulty
        self.q = str(q)
        self.ans = str(ans)
        self.option1 = str(option1)
        self.option2 = str(option2)
        self.option3 = str(option3)
        self.option4 = str(option4)

    def debug(self):
        print("題號:"+self.q_number+"  難度："+self.q_difficulty)
    def print_question(self):
        print("")
        print("題號:"+self.q_number+"  難度："+self.q_difficulty+"  題型："+self.q_type)
        print("Q:"+self.q)
        print("選項:")
        print("1:" + self.option1)
        print("2:" + self.option2)
        print("3:" + self.option3)
        print("4:" + self.option4)
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ans:"+self.ans)

book = pe.get_book(file_name="exam.xlsx")
sheet = book.sheet_by_index(0)

questions= list()
diff = list()

diff.append(list()) #hard
diff.append(list()) #mid
diff.append(list()) #easy



for index in range(0,750):
    questions.append(question(
        number = sheet[index*7,1],
        type = sheet[index*7,8],
        difficulty = sheet[index*7,11],
        q = sheet[index*7+1,1],
        ans = sheet[index*7+2,1],
        option1 = sheet[index*7+3,1],
        option2 = sheet[index*7+4,1],
        option3 = sheet[index*7+5,1],
        option4 = sheet[index*7+6,1]
    ))
    if(questions[-1].q_difficulty == "難"):
        diff[0].append(index)
    elif(questions[-1].q_difficulty == "中"):
        diff[1].append(index)
    else:
        diff[2].append(index)

practice_number = int(input("請輸入你要練習之題目數量"))
practice_diff = int(input("請輸入你要練習之難度 1->難 2->中 3->簡單"))
for index in random.sample(diff[practice_diff-1],practice_number):
    questions[index].print_question()