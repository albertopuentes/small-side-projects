import time
from playsound import playsound
    
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(2)
        t -= 1
    playsound('/Users/albertopuentes/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/Tolling_Bell.wav')
    print('Timer Completed')
    

t = input("Enter the time in seconds: ")

countdown(int(t))