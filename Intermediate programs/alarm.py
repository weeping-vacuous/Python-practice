import time
import datetime
import pygame

def set_alarm(alrm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "D:\\python\\Intermediate programs\\alarm.mp3"
    is_running = True

    while is_running:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)

        if now == alrm_time:
            print("WAKE UP!!😫")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)


       

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in (HH:MM:SS): ")
    if not len(alarm_time) == 8:
        print("Invalid time format. Please use HH:MM:SS format.")
    elif int(alarm_time[0:2])>23 or int(alarm_time[3:5])>59 or int(alarm_time[6:8])>59:
        print("Invalid time. Please enter a valid time.")
    elif not(alarm_time[2]==':' and alarm_time[5]==':'):
        print("Invalid time format. Please use HH:MM:SS format.")
    elif not alarm_time.replace(":","").isdigit():
        print("Invalid time. Please enter numeric values only.")
    elif alarm_time == datetime.datetime.now().strftime("%H:%M:%S"):
        print("The alarm time cannot be the current time. Please set a future time.")
    elif alarm_time < datetime.datetime.now().strftime("%H:%M:%S"):
        print("The alarm time cannot be in the past. Please set a future time.")
    else:
      set_alarm(alarm_time)