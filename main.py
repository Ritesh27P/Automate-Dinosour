from PIL import ImageGrab
import pyautogui
import webbrowser
import time

webbrowser.open('http://google.com')  


pyautogui.FAILSAFE = False;
x, y = 794, 273; 
# print(pyautogui.position());

# pyautogui.moveTo(x, y);   
time.sleep(2)
pyautogui.press('space') 
# time.sleep(5);
while True: 
    im = ImageGrab.grab( bbox = (794, 283, 796, 286))  
    if im.getpixel((0, 0))  == (172, 172, 172):
        pyautogui.press('space');

 