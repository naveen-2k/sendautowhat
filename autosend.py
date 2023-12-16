import time
import webbrowser
import pyautogui
import keyboard
from datetime import datetime, timedelta



def is_matching_time(target_hour, target_minute):
    current_time = datetime.now().time()
    return current_time.hour == target_hour and current_time.minute == target_minute

def wait_until_matching_time(target_hour, target_minute):
    while not is_matching_time(target_hour, target_minute):
        
        current_time = datetime.now().time()
        current_datetime = datetime.now()
        target_datetime = datetime(current_datetime.year, current_datetime.month, current_datetime.day, target_hour, target_minute)
        
        if current_datetime > target_datetime:
            # If the target time has already passed today, calculate the time until the next day
            target_datetime += timedelta(days=1)
        
        time_difference = target_datetime - current_datetime
        seconds_to_wait = time_difference.total_seconds()
        print(f"wait for {seconds_to_wait}")
        time.sleep(seconds_to_wait)




def send_whatsapp_message(contact_name, message):
    # Open WhatsApp Web in the default web browser
    #webbrowser.open("https://web.whatsapp.com")
    webbrowser.open(f"https://web.whatsapp.com/send?phone=+91{contact_name}")
    
    
    
    # Focus on the chat search input field
    # keyboard.press_and_release('ctrl+f')
    # time.sleep(2)
    
    # Type the contact name and press Enter
    # keyboard.write(contact_name)
    # time.sleep(2)
    # keyboard.press_and_release('enter')
    
    # Allow some time for the chat to load
    time.sleep(15)
    
    # Type and send the message
    # keyboard.write(message)
    pyautogui.write(message)
    print("written")
    time.sleep(1)
    pyautogui.press('enter')
    print("executed")
   
    # keyboard.press_and_release('enter')

def getin():
    print("""-------write a message schedule later-------
    |Then enter hour and minutes(24hrs format)|""")
    number=input("Enter the recepients phone number (10digit):")
    message=input("Enter what you want to say:")
    hour=int(input("Enter the hour:"))
    minutes=int(input("Enter minute:"))

    if len(number)!=10:
        print("Invalid Phone Number")
        getin()
    if hour<0 | hour>23 | minutes>59 | minutes<0:
        print("Invalid Time Format")
        getin()

    print("Waiting for the target time...")
    wait_until_matching_time(hour,minutes)
    print("Current time now matches the target time.")
    send_whatsapp_message(number, message)
    
getin()

