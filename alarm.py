#!/usr/bin/env python


import schedule
import subprocess
import time


def job():
    subprocess.call(['aplay /home/pi/alarm.wav'], shell=True)


schedule.every().day.at('7:00').do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
