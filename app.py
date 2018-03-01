from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

#### QUIZ CLASS ####

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

    locationDesc = ["Yellowknife Bay", "Darwin", "Cooperstown", "Kimberley", "Pahrump Hills", "Yellowknife Bay",
                    "Darwin", "Cooperstown", "Kimberley", "Pahrump Hills"]

    def __init__(self, index):
        self.index = index

    def getAnswer(self, index):
        return self.answerValue[index]

    def nextQuestion(self):
        self.index = self.index + 1

    def noOfQuestions(self):
        return len(self.answerValue)


#### IMAGESOURCER CLASS ####

class ImageSourcer:

    # Constructor initialising attributes
    def __init__(self, rover, sol, index):
        apiKey = "lORFMg7rox7XMLBWzM1byE9fd5WAe3Cf9KkoQYmp"
        self.rover = rover
        self.sol = sol
        self.responseString = ("https://api.nasa.gov/mars-photos/api/v1/rovers/" + self.rover + "/photos?sol="
                              + self.sol + "&api_key=" + apiKey)
        self.index = index

    def __call__(self):
        return (self.index)

    # Write links to images to text file
    '''def writeToFile(self, data, fileName):
        textFile = open(fileName, "w")
        for entry in data["photos"]:
            print(entry["img_src"])
            textFile.write(entry["img_src"])
            textFile.write("\n")'''

    def returnURL(self, data):
        return data["photos"][self.index]["img_src"]

    # Send API request for JSON object
    def receiveImages(self):
        response = requests.get(self.responseString)

        # Check to see if request OK
        if (response.status_code != 200):
            print ("API Request failed")
        else:
            data = response.json()

            # Create file name and store in folder 'images'
            fileName = self.rover + "-" + self.sol + ".txt"
            completeFileName = os.path.join("images/", fileName)

            # Remove file if already exists for parameters, to allow new data
            # to be retrieved
            if (os.path.isfile(completeFileName)):
                os.remove(completeFileName)
            else:
                return self.returnURL(data)

quizInit = Quiz(0)

#### WEB STUFF ####

@app.route("/")
def initialise():
    return render_template('signup.html')


@app.route("/loggedin")
def intro():
    return render_template('intro.html')


@app.route("/start")
def renderQuestion(valid):
    index = quizInit.index
    nowValid = valid
    print(nowValid)
    imgRequest = ImageSourcer("Curiosity", "1350", index)
    x = imgRequest()
    link = imgRequest.receiveImages()
    return render_template('screenload.html', challenge=quizInit.questions[index], optA=quizInit.optionsA[index],
                           optB=quizInit.optionsB[index], optC=quizInit.optionsC[index], optD=quizInit.optionsD[index],
                           qNo=(quizInit.index+1), myLink=link, mapVal=quizInit.locationDesc[index], msgEnable=nowValid)


@app.route("/help")
def help():
    return render_template('help.html')

@app.route("/gameover")
def gameOver():
    return render_template('win.html')

@app.route("/correct")
def correct():
    return render_template('correct.html')

@app.route("/redirect")
def redirect():
    return renderQuestion("true")


@app.route("/submit", methods=['GET', 'POST'])
def quizManage():
    if request.method == 'POST':

        try:
            result = request.form['options']
            if result == quizInit.getAnswer(quizInit.index):
                print("CORRECT")
                quizInit.nextQuestion()
                if quizInit.index == (quizInit.noOfQuestions()):
                    #print("DONE")
                    return gameOver()
                return correct()
            else:
                print("INCORRECT")
                return renderQuestion("false")
        except:
            return renderQuestion("false")


if __name__ == "__main__":
    app.run()
