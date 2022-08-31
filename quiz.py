#read questions from file and add to list
def readQuestions():
    questionList = []
    question = open("questions.txt", "r")

    line = question.readline()
    line = line.rstrip("\n")

    while line != "":
        questionList.append (line)
        line = question.readline()
        line = line.rstrip("\n")
    
    return questionList

def readList(questionList):
    print(questionList)

def startQuiz(questionList):
    for question in questionList:
        
        answer = input(question)


def main():
    catchQuestionList = []
    catchQuestionList = readQuestions()
    readList(catchQuestionList)
    catchCount = []
    catchCount = readQuestions()
    startQuiz(catchQuestionList)

    

main()
#

