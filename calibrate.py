from time import sleep
import pyautogui as gui


def showPosition():
    pos = gui.position()
    print('x:', pos.x, 'y:', pos.y)


if __name__ == '__main__':
    while True:
        showPosition()
        sleep(1.0)
        