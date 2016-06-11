#Convert the function convertToSeconds to a method in the Time class.

class Time:
    def __init__(self, seconds=0,minutes=0,hours=0):
        self.seconds=seconds
        self.minutes=minutes
        self.hours=hours
        
    def convertToSeconds(self):
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds

#Add a fourth parameter, end, to the find function that specifies where to stop looking.

def find(str, ch, start=0, end=None):
    index = start
    if end == None:
        end = len(str)
    while index < end:
        if str[index] == ch:
            return index
        index = index + 1
    return -1
