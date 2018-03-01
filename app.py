from flask import Flask, render_template, request

app = Flask(__name__)


class Quiz:
    index = 0
    answerValue = ["b", "d", "c", "c", "b", "a", "d", "b", "d", "a"]
    questions = ["Which star is at the centre of the Solar System?",
                 "What percent of the solar system's mass does the Sun hold?",
                 "How many stars are in the Milky Way?",
                 "How long ago was the Sun formed?",
                 "How much time does it take for sun rays to reach Earth?",
                 "Which planet has the most moons in the solar system?",
                 "What is the average surface temperature of the Moon during the day?",
                 "Which of the planets have rings around them?",
                 "How fast do rockets travel in space?",
                 "What is the closest planet to the Sun?"]
    
    optionsA = ["Milky Way", "47.1%", "50 million", "5000 years ago", "30 seconds", "Jupiter", "49ºC", "Earth",
                "100 mph", "Mercury"]
    optionsB = ["Sun", "96.5%", "200000", "6.3 million years ago", "8 minutes", "Mars", "592ºC", "Saturn", "500mph",
                "Pluto"]
    optionsC = ["Katy Perry", "10.3%", "100 billion", "4.6 billion years ago", "23 minutes", "Neptune", "271ºC",
                "Mercury", "14000mph", "Uranus"]
    optionsD = ["Moon", "99.8%", "2000 billion (a lot)", "70 trillion years ago", "1 and a half hours", "Uranus",
                "107ºC", "Venus", "20000mph", "Mars"]

    def __init__(self, index):
        self.index = index

    def getAnswer(self, index):
        return self.answerValue[index]

    def nextQuestion(self):
        self.index = self.index + 1

    def noOfQuestions(self):
        return len(self.answerValue)


quizInit = Quiz(0)


@app.route("/")
def initialise():
    return render_template('signup.html')


@app.route("/loggedin")
def intro():
    return render_template('intro.html')


@app.route("/start")
def renderQuestion():
    index = quizInit.index
    return render_template('screenload.html', challenge=quizInit.questions[index], optA=quizInit.optionsA[index],
                           optB=quizInit.optionsB[index], optC=quizInit.optionsC[index], optD=quizInit.optionsD[index],
                           qNo=(quizInit.index+1))


@app.route("/help")
def help():
    return render_template('help.html')


@app.route("/submit", methods=['GET', 'POST'])
def quizManage():
    if request.method == 'POST':

        '''# return result
        if result == quizInit.getAnswer(quizInit.index):
            print("CORRECT")
            print(quizInit.index)
            quizInit.nextQuestion()
            if quizInit.index == quizInit.noOfQuestions():
                print("DONE")
                return render_template("help.html")
            return renderQuestion()
        else:
            print("INCORRECT")
            return renderQuestion()
        # return render_template('help.html')'''

        try:
            result = request.form['options']
            if result == quizInit.getAnswer(quizInit.index):
                print("CORRECT")
                print(quizInit.index)
                quizInit.nextQuestion()
                if quizInit.index == quizInit.noOfQuestions():
                    print("DONE")
                    return render_template("help.html")
                return renderQuestion()
            else:
                print("INCORRECT")
                return renderQuestion()
        except:
            return renderQuestion()


if __name__ == "__main__":
    app.run()
