from PIL import ImageGrab
import pyautogui
import webbrowser
import time

webbrowser.open('http://google.com')  


pyautogui.FAILSAFE = False;
x, y = 723, 291;
# pyautogui.moveTo(x, y);  
time.sleep(10);
pyautogui.press('space') 

for i in range(10):
    im = ImageGrab.grab( bbox = (680, 200, 880, 350)) 
    px = im.load()
    coordinate = x, y = 150, 75; 
    pixels = im.getpixel(coordinate)
    print(pixels)
    if pixels == (17, 25, 25):
        print('cactus');

 
    

# pyautogui.click(500, 500)
# pyautogui.press('space')


 