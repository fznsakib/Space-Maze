class Quiz:
    question = 0
    answers = ["b", "d", "c", "c", "b", "a", "d", "b", "a", "a"]

    def __init__(self, question):
        self.question = question


    def getAnswer(self, index):
        return self.answers[index]

    def nextQuestion(self):
        self.question = self.question + 1

    def noOfQuestions(self):
        return len(self.answers)