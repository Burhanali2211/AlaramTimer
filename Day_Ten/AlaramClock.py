import time
import datetime
from playsound import playsound

def countdown_timer(alarm_time):
    while True:
        current_time = datetime.datetime.now()
        remaining_time = alarm_time - current_time
        
        if remaining_time.total_seconds() <= 0:
            break
        
        print(f"⏳ Time left for alarm: {str(remaining_time).split('.')[0]}", end="\r")
        time.sleep(1)

def set_alarm(delay, alarm_sound):
    current_time = datetime.datetime.now()
    alarm_time = current_time + datetime.timedelta(seconds=delay)
    
    print(f"\nAlarm will ring at {alarm_time.strftime('%H:%M:%S')} ⏳")
    countdown_timer(alarm_time)  # Show countdown

    print("\n⏰ Alarm ringing! Wake up! ⏰")
    playsound(alarm_sound)  # Play alarm sound

# User input for alarm delay
delay = int(input("Enter time delay for alarm (in seconds): "))

# User input for alarm sound
alarm_sound = input("Enter alarm sound file (e.g., alarm.mp3, wav): ")

set_alarm(delay, alarm_sound)
