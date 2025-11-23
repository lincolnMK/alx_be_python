from datetime import date
from datetime import timedelta
from datetime import datetime


def  display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date    

def calculate_future_date():
    days_ahead = int(input ("Enter the number of days to add to the current date:"))
    current_date = date.today()
    future_date = current_date + timedelta(days=days_ahead)
    return future_date
    
current_date =  display_current_datetime()
print("Current Date and Time:", current_date )
future_date = calculate_future_date()
print ("Future date:", future_date)