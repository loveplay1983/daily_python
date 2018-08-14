import pyautogui
import subprocess
import os
import time

time.sleep(5)
subprocess.Popen('mspaint')
pyautogui.moveTo(100, 100, 0.1)
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
time.sleep(5)
subprocess.Popen('mspaint')
pyautogui.moveTo(500, 100, 3)

time.sleep(1)
pyautogui.hotkey('alt', 'f4')