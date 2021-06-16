import winsound


def fileCheck(fileName):
    try:
        open(fileName, "r")
        return 1
    except FileNotFoundError:
        print("Error: File does not appear to exist.")
        return 0


def play(fileName):
    if fileCheck(fileName):
        # Plays the audio               to play it while you are gamer
        winsound.PlaySound(fileName, winsound.SND_ASYNC)


def playRep(fileName):
    if fileCheck(fileName):
        # Plays the audio               to play it while you are gamer
        winsound.PlaySound(fileName, winsound.SND_ASYNC | winsound.SND_LOOP)
