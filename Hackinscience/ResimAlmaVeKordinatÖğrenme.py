from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
from time import sleep
de=[180,200,350,470]
def cv2img():
    den = np.array(ImageGrab.grab(de))
    den=cv2.cvtColor(den,cv2.COLOR_RGB2BGR)
    cv2.imshow("",den)
    cv2.waitKey(0)
def imgrab():
    img=ImageGrab.grab(de)
    img.show()
def userinput():
    global a
    a=int(input("Resmi pil(1) ile mi cv2(2) ile mi görüntülemek istersiniz , yada 4 kordinatı 3 sn ara ile öğrenmek için (3) sürekli koordinat görmek için (4):"))
    return a
def play():
    userinput()
    if a==1:
        imgrab()
    if a==2:
        cv2img()
    if a==3:
        sleep(3)
        for i in range(4):
            print(pyautogui.position())
            sleep(3)
    if a==4:
        pyautogui.displayMousePosition()
play()


