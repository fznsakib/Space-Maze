class Quiz:
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

    locationDesc = ["Yellowknife Bay", "Darwin", "Cooperstown", "Kimberley", "Bridger Basin", "Gobabeb",
                    "Naukleft Plateau", "Murray Buttes", "Ogunquit Beach", "Vera Rubin Ridge"]

    facts = ["One year on Earth is the same as 12 years on Jupiter!",
             "The Sun is about 330,000 times the mass of our planet, Earth!",
             "Looking at a far away star is the same as looking back through time, because it takes so long for the light to travel to us!",
             "The Sun has about 5 billion more years of fuel left in it before it dies",
             "Currently, the Sun is a yellow dwarf star",
             "Jupiter has a whopping 63 moons orbiting it! Wowza!",
             "At night, the Moon can be as cold as -180ºC",
             "Saturn is less dense than water, meaning it would float if it were in a bathtub large enough to hold it!",
             "One rocket uses up enough fuel to power 86,000 houses for a day!",
             "Pluto, once thought to be the furthest planet in our solar system, is no longer thought to be a planet because it is simply too small!"]

    links = ["https://en.wikipedia.org/wiki/Yellowknife_Bay,_Mars",
              "https://en.wikipedia.org/wiki/Darwin_(Martian_crater)",
              "https://www.jpl.nasa.gov/news/news.php?feature=3936",
              "https://www.nasa.gov/jpl/msl/pia18075/#.WpeMCOjFKUk",
              "https://www.nasa.gov/jpl/mro/pia19114",
              "https://www.nasa.gov/image-feature/jpl/pia20174/marias-pass-contact-zone-of-two-martian-rock-units",
              "https://mars.nasa.gov/msl/mission/mars-rover-curiosity-mission-updates/?mu=sol-1094-turning-in-to-bridger-basin",
              "http://redplanet.asu.edu/?tag=gobabeb",
              "https://www.nasa.gov/image-feature/pia20332/full-circle-vista-from-naukluft-plateau-on-mars",
              "https://mars.nasa.gov/msl/curiosity-murray-buttes-raw-images/"]

    roverImages= [("1400", 0), ("1400", 1), ("1400", 2), ("1400", 3), ("1400", 4), ("1350", 1), ("620", 1), ("620", 2),
                  ("1400", 6), ("1400", 5)]

    def __init__(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def getAnswer(self):
        return self.answerValue[self.index]

    def nextQuestion(self):
        self.index = self.index + 1

    def noOfQuestions(self):
        return len(self.answerValue)

    def progress(self):
        return (self.index)*10

    # Quiz webpage requires a lot of different data to show current question. This method puts it all in one array
    # to be fed into HTML file
    def currentQuizState(self):
        index = self.index

        array = [self.questions[index], self.optionsA[index], self.optionsB[index], self.optionsC[index],
                 self.optionsD[index], self.index+1, self.locationDesc[index], self.progress(), self.facts[index],
                 self.links[index]]

        return array
