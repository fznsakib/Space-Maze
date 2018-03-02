class Quiz:

    keys = ["answer", "question", "optionA", "optionB", "optionC", "optionD", "location", "fact", "link"]
    dataDicts = []

    roverImages = [("1400", 0), ("1400", 1), ("1400", 2), ("1400", 3), ("1400", 4), ("1350", 1), ("620", 1), ("620", 2),
                  ("1400", 6), ("1400", 5)]

    def __init__(self, index):
        self.index = index

        # Read data from text file into dictionary dataDicts
        with open("data.txt") as f:
            for line in f:
                # Split each line in terms of where comma is found
                line = line.strip().split(', ')
                # Create a dictionary  for each row.
                d = dict(zip(self.keys, line))
                # Store for future use
                self.dataDicts.append(d)

        print(self.dataDicts)
        
    def getIndex(self):
        return self.index

    def getAnswer(self):
        return self.dataDicts[self.index].get("answer")

    def nextQuestion(self):
        self.index = self.index + 1

    def noOfQuestions(self):
        return len(self.dataDicts)

    def progress(self):
        return (self.index)*10

    # Quiz webpage requires a lot of different data to show current question. This method puts it all in one array
    # to be fed into HTML file
    def currentQuizState(self):
        progress = self.progress()
        index = self.index
        data = self.dataDicts[index]

        array = [data.get("question"), data.get("optionA"), data.get("optionB"), data.get("optionC"),
                 data.get("optionD"), index+1, data.get("location"), progress, data.get("fact"),
                 data.get("link")]

        return array
