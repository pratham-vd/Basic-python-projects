import time

print("Simple Alarm Clock")

alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M")   
    
    if current_time == alarm_time:
        print("\n ALARM! Time's up! \n")
        break

    time.sleep(1)  
