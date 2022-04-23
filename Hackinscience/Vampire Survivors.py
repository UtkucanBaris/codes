import keyboard
import time
from pyautogui import click
t = input("Enter the time in seconds: ")
y=0
while y<80:
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            click()
          
        print('Fire in the hole!!')
        exit()
    countdown(int(t))
    y+=1