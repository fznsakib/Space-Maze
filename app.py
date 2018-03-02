from flask import Flask, render_template, request
import quiz, imageSourcer


app = Flask(__name__)

mainQuiz = quiz.Quiz(0)

#### WEB STUFF ####

@app.route("/")
def initialise():
    return render_template('signup.html')


@app.route("/loggedin")
def intro():
    return render_template('intro.html')


@app.route("/start")
def renderQuestion(valid):
    (imgSol, imgIndex) = mainQuiz.roverImages[mainQuiz.getIndex()]
    imgRequest = imageSourcer.ImageSourcer("Curiosity", imgSol, "navcam", imgIndex)
    x = imgRequest()
    link = imgRequest.receiveImages()
    quizData = mainQuiz.currentQuizState()
    return render_template('screenload.html', challenge=quizData[0], optA=quizData[1], optB=quizData[2],
                           optC=quizData[3], optD=quizData[4], qNo=quizData[5], mapVal=quizData[6],
                           progressValue=quizData[7], myLink=link, msgEnable=valid)


@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/gameover")
def gameOver():
    return render_template('win.html')

@app.route("/correct")
def correct():
    quizData = mainQuiz.currentQuizState()
    return render_template('correct.html', mapVal=quizData[6], fact=quizData[8], wikiLink=quizData[9])

@app.route("/redirect")
def redirect():
    return renderQuestion("false")


@app.route("/submit", methods=['GET', 'POST'])
def quizManage():
    # Check for user input
    if request.method == 'POST':

        try:
            # If input chosen is correct answer then move on to next question
            result = request.form['options']
            if result == mainQuiz.getAnswer():
                mainQuiz.nextQuestion()
                # If all questions attempted the game is over
                if mainQuiz.getIndex() == (mainQuiz.noOfQuestions()):
                    mainQuiz.index = 0
                    return gameOver()
                return correct()
            else:
                # Input chosen is incorrect, show relevant message and allow user to try again
                return renderQuestion("true")
        except:
            # If no input chosen, allow user to try again
            return renderQuestion("true")


if __name__ == "__main__":
    app.run()
