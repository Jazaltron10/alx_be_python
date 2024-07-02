from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.today()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
display_current_datetime()

# Part 2: Calculate a Future Date
def calculate_future_date():
    number_of_days = int(input("\nEnter the number of days to add to the current date: "))
    today_date = datetime.now()
    future_date = today_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")
    
calculate_future_date()