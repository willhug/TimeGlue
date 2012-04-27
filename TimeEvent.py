import datetime as dt

#Hold information on the time event
class TimeEvent:
  def __init__(self,
              name,
              priority=5,
              event_type='work',
              start_date=dt.date.today(),
              end_date=None):
    self.name = name
    self.priority = priority
    self.event_type = event_type
    self.start_date = start_date
    self.end_date = end_date
