import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds >0:
        print(f'Time remaining: {seconds // 60}:{seconds % 60:02d}')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

focus_time = int(input("Enter the focus time in minutes: "))
focus_timer(focus_time)
