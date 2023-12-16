import pywhatkit as wk

def getin():
    print("""-------write a message schedule later-------
    |Then enter hour and minutes(24hrs format)|""")
    number=input("Enter the recepients phone number (10digit):")
    msg=input("Enter what you want to say:")
    hour=int(input("Enter the hour:"))
    minutes=int(input("Enter minute:"))

    if len(number)!=10:
        print("Invalid Phone Number")
        getin()
    if hour<0 | hour>23 | minutes>59 | minutes<0:
        print("Invalid Time Format")
        getin()

    wk.sendwhatmsg("+91"+number,msg,int(hour),int(minutes))
getin()