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
    answerlist = []

    for question in questionList:
        answer = input(question)
        answerlist.append(answer)

    return answerlist    

def determineClass(total):
    userclass = ""
    if total < 6:
        userclass = "bard"
    elif total < 11:
        userclass = "wizard"
    elif total < 16:
        userclass = "rouge"
    else:
        userclass = "barbarian"      

    return userclass

def processAnswer(answerList):
    total = 0
    for currentNumber in answerList:
        total = total + int(currentNumber)

    return total    

def main():
    catchQuestionList = []
    catchQuestionList = readQuestions()
    catchAnswerList = []

    catchAnswerList = startQuiz(catchQuestionList)
    total = processAnswer(catchAnswerList)
    userclass = determineClass(total) 
    print("You are a " + userclass)
    
main()
#

