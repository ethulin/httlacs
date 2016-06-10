#Write a function print_time that takes a Time object as an argument and prints it in the form hours:minutes:seconds.

class Time:
    def __init__(self, seconds=0,minutes=0,hours=0):
        self.seconds=seconds
        self.minutes=minutes
        self.hours=hours
        
def print_time(time):
    print '{}:{}:{}'.format(time.hours, time.minutes, time.seconds)

#Write a boolean function after that takes two Time objects, t1 and t2, as arguments, and returns True if t1 follows t2 chronologically and False otherwise.

def convert_to_seconds(time):
    return time.seconds + time.minutes * 60 + time.hours * 60 * 60

def first_time_later(t1, t2):
    if convert_to_seconds(t1) > convert_to_seconds(t2):
        return True
    else:
        return False

#Rewrite the increment function so that it doesn't contain any loops.

def convert_to_time(seconds):
    time = Time()
    time.hours = seconds / 60 / 60
    time.minutes = (seconds - time.hours * 60 * 60) / 60
    time.seconds = seconds - time.hours * 60 * 60 - time.minutes *60
    return time

def increment(time,seconds):
    return convert_to_time(convert_to_seconds(time)+seconds)
