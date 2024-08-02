def getHighScore():
    userFile = open("userData", "r")
    return userFile.read().split("\n")[0].split(" ")[1]

def saveHighScore(score):
    userFile = open("userData", "r+")
    fileContents = userFile.read().split("\n")
    fileContents[0] = f'score {score}'
    userFile.write("\n".join(fileContents))