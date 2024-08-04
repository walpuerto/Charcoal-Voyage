import simpleaudio

mainMenu_obj = simpleaudio.WaveObject.from_wave_file('resources\main menu.wav')
mainMenu_play = None

leadingMusic = None

def playMainMenu():
    global mainMenu_play
    mainMenu_play = mainMenu_obj.play()

    global leadingMusic
    leadingMusic = mainMenu_play

def stopLeadingMusic():
    mainMenu_play.stop()

beep_obj = simpleaudio.WaveObject.from_wave_file('resources\\beep short.wav')

def playBeep():
    beep_obj.play()

beepHigh_obj = simpleaudio.WaveObject.from_wave_file('resources\\beep high.wav')

def playBeepHigh():
    beepHigh_obj.play()

beepLong_obj = simpleaudio.WaveObject.from_wave_file('resources\\beep long.wav')

def playBeepLong():
    beepLong_obj.play()

matthew_obj = simpleaudio.WaveObject.from_wave_file('resources\where is matthew.wav')

def playMatthew():
    global leadingMusic
    leadingMusic = matthew_obj.play()

shower_obj = simpleaudio.WaveObject.from_wave_file('resources\meteor shower.wav')

def playShower():
    global leadingMusic
    leadingMusic = shower_obj.play()