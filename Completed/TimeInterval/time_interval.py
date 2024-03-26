import datetime

class TimeInterval:
  def __init__(self,hours,minutes,seconds):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds
    try:
      self.total_seconds = (int(hours)*3600) + (int(minutes)*60) + int(seconds)
    except ValueError:
      raise ValueError("Invalid Time Format")

  def __add__(self, other): # adding the seconds from the times given
    total_seconds = self.total_seconds + other.total_seconds
    return TimeInterval(0, 0, total_seconds)

  def __sub__(self, other): # subtracting the seconds from the given times
    total_seconds = self.total_seconds - other.total_seconds
    return TimeInterval(0, 0, total_seconds)

  def __mul__(self, x): # multplying the seconds from the given time.
    total_seconds = self.total_seconds * x
    return TimeInterval(0, 0, total_seconds)


  def __str__(self): # used when called in print(str(...))
    return str(datetime.timedelta(seconds = self.total_seconds))

def main():
  try:
    hour1, min1, sec1 = input("First-Time (HH:MM:SS): ").split(":")
    hour2, min2, sec2 = input("Second-Time (HH:MM:SS): ").split(":")
  except ValueError:
    print("Invaid format entered.")
    return  
    
  t1 = TimeInterval(hour1,min1, sec1)
  t2 = TimeInterval(hour2,min2, sec2)

  print(f"2x - Multiplied time",t1 * 2)
  print(f"Total time added:",str(t1 + t2))
  print(f"Remaining time :",str(t1 - t2))


main()
