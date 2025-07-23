from multiprocessing import Process
import keyboard
import time
import pyautogui

def auto(t):
    while True:
        pyautogui.click()
        time.sleep(t)
        

if __name__ == '__main__':
    t = int(input())
    process = Process(target=auto)
    process.start()
    while process.is_alive():
        if keyboard.is_pressed('q'):
            process.terminate()
            break
