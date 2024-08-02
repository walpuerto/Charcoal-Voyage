def getHighScore():
    userFile = open("userData.cvoyage", "r")
    return int(userFile.read().split("\n")[0].split(" ")[1])

def saveHighScore(score):
    userFile = open("userData.cvoyage", "r+")
    fileContents = userFile.read().split("\n")
    fileContents[0] = f'score {score}'
    userFile.seek(0)
    userFile.truncate(0)
    userFile.write("\n".join(fileContents))

def getTimesPlayed():
    userFile = open("userData.cvoyage", "r")
    return int(userFile.read().split("\n")[1].split(" ")[1])

def incrementTimesPlayed():
    userFile = open("userData.cvoyage", "r+")
    fileContents = userFile.read().split("\n")
    fileContents[1] = f'timesPlayed {int(fileContents[1].split(" ")[1]) + 1}'
    userFile.seek(0)
    userFile.truncate(0)
    userFile.write("\n".join(fileContents))