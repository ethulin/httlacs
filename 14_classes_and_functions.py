#Write a function print_time that takes a Time object as an argument and prints it in the form hours:minutes:seconds.

class Time:
    def __init__(self, seconds, minutes, hours):
        self.seconds=seconds
        self.minutes=minutes
        self.hours=hours
        
def print_time(time):
    print '{}:{}:{}'.format(time.hours, time.minutes, time.seconds)

#Write a boolean function after that takes two Time objects, t1 and t2, as arguments, and returns True if t1 follows t2 chronologically and False otherwise.

minutes_in_hour = 60
seconds_in_minute = 60

def convert_to_seconds(time):
    return time.seconds + time.minutes * seconds_in_minute + time.hours * minutes_in_hour * seconds_in_minute

def first_time_later(t1, t2):
    if convert_to_seconds(t1) > convert_to_seconds(t2):
        return True
    else:
        return False

#Rewrite the increment function so that it doesn't contain any loops.

def convert_to_time(seconds):
    time = Time()
    time.hours = seconds / minutes_in_hour / seconds_in_minute
    time.minutes = (seconds - time.hours * minutes_in_hour * seconds_in_minute) / seconds_in_minute
    time.seconds = seconds - time.hours * minutes_in_hour * seconds_in_minute - time.minutes * seconds_in_minute
    return time

def increment(time,seconds):
    return convert_to_time(convert_to_seconds(time)+seconds)
