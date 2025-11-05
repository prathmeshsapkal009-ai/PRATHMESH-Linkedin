from plyer import notification as ntf
import pyttsx3
import time
import schedule
def reminder():
    ntf.notify(title="Water Reminder",message="Drink water ASAP",timeout=4)
    engine=pyttsx3.init()
    engine.say("Drink water asap")
    engine.runAndWait()
# schedule.every().day.at("17:07").do(reminder)
schedule.every(10).seconds.do(reminder)
# schedule.every(1).hour.do(reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
# print(dir(schedule))
# print(schedule.datetime.time)