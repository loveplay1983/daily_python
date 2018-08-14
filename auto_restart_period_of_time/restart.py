import os
import time
import psutil

import subprocess


app_path = r'C:\Users\John\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'
t = 10

while True:

    time.sleep(t)
    for i in psutil.process_iter():
        if i.name() == '360chrome.exe':
            # print ('a')
            i.kill()
    # print ('b')
    time.sleep(t)
    subprocess.Popen(app_path)
