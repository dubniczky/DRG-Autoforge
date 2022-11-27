import sys
from time import sleep
import pyautogui as gui


points = {
    'item': (2795, 761), # Select top item to craft
    'start': (1907, 1327), # Start crafting
    'confirm': (1907, 1327), # Accept selected item
}


def forgeCycle():
    # Select item to craft
    gui.moveTo(points['item'][0], points['item'][1], duration=0.25)
    gui.click()
    
    # Start crafitng
    gui.moveTo(points['start'][0], points['start'][1], duration=0.25)
    gui.click()
    sleep(18.0)
    
    # Confirm received items
    gui.moveTo(points['confirm'][0], points['confirm'][1], duration=0.25)
    gui.click()
    sleep(3.0)


def forgeLoop(limit = -1):
    i = 0
    while True:
        if limit > 0 and i >= limit:
            break
        
        print('Cycle:', (i+1))
        forgeCycle()
        sleep(0.5)
        i += 1


if __name__ == '__main__':
    if len(sys.argv) > 2:
        forgeLoop(int(sys.argv[2]))
    else:
        forgeLoop()
