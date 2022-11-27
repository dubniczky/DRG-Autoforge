from time import sleep
import pyautogui as gui

width, height = gui.size()

print(gui.position())

# top core position on screen: Point(x=2795, y=761)
# start craft position on screen: Point(x=1907, y=1327)

def forgeLoop():
    # Select item to craft
    gui.moveTo(2795, 761, duration=0.25)
    gui.click()
    
    # Start crafitng
    gui.moveTo(1907, 1327, duration=0.25)
    gui.click()
    
    sleep(18.0)
    
    gui.moveTo(1907, 1327, duration=0.25)
    gui.click()
    
    sleep(3.0)
    
    
for i in range(0, 100):
    forgeLoop()