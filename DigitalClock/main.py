

class DigitalClock:

  def __init__(self, hours: int, minutes: int):
    """Constructor method"""
    self.hours = hours
    self.minutes = minutes

  def get_time(self):
    """Get time now"""
    return f"{self.hours}:{self.minutes}"

  def set_hours(self, hours):
    """Set custom hour"""
    self.hours = hours

  def set_minutes(self, minutes):
    """Set custom minute"""
    self.minutes = minutes

  def increment_minutes(self):
    """Increment minute by one"""
    self.minutes += 1
    
    if self.minutes == 60:
      self.minutes = 0
      self.hours += 1
    if self.hours >= 24:
      self.hours -= 24

# Create instance of class
clock = DigitalClock(25, 20)
clock.increment_minutes()
print(tn)
print(clock.get_time())