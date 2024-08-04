import simpleaudio

mainMenu_obj = simpleaudio.WaveObject.from_wave_file('resources\main menu_01.wav')
mainMenu_play = None

def playMainMenu():
    mainMenu_play = mainMenu_obj.play()

def stopMainMenu():
    mainMenu_play.stop()