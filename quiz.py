#read questions from file and add to list
def readQuestions():
    questionList = []
    question = open("questions.txt", "r")

    line = question.readline()
    line = line.rstrip("\n")

    while line != "":
        questionList.append(line)
        line = question.readline()
        line = line.rstrip("\n")
    
    return questionList

def readList(questionList):
    print(questionList)

def startQuiz(questionList):
    
    
    for question in questionList:
        answer = input(question)
'''   
    return answer    

def writeAnswer(answer):
    count = 0
    answer = open("score.txt", "x")
'''
    
def main():
    catchQuestionList = []
    catchQuestionList = readQuestions()
    readList(catchQuestionList)
    startQuiz(catchQuestionList)

    
main()
#

