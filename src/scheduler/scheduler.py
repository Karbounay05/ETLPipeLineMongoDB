import schedule
import time

from src.main import main

schedule.every(1).minutes.do(main)

print("Scheduler started...")

while True:

    schedule.run_pending()

    time.sleep(1)