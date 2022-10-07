class Event:
    def __init__(self, event_type, event_time):
        self.event_type = event_type  # Event type of ARRIVAL, DEPART, or OBSERVATIONS
        self.event_time = event_time  # Respective event time

    def __lt__(self, other):
        return self.event_time < other.event_time  # Less than operator for heappush
