from datetime import *

def add_gigasecond(birth_date):
   gigasecond = 10 ** 9
   return  birth_date + timedelta(seconds=gigasecond)

def calculate_time(time):
    days = time // (24 * 60 * 60)
    time %= 24 * 60 * 60
    hours = time // (60*60)
    time %= 60 * 60
    minutes = time // (60)
    time %= 60
    seconds = time
    return (days, hours, minutes, seconds)


