"""
Utilities 
"""
# utils.py

import datetime

def unix_timestamp_decode(timestamp):
    """Takes UNIX time stamp as input and returns a datetime object based on that

    Args:
        timestamp (int): UNIX Time stamp
    """
    timestamp_ms = timestamp
    # Convert milliseconds to seconds
    timestamp_s = timestamp_ms / 1000
    # Convert the timestamp to a datetime object
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp_s)
    return datetime_obj

def compare_h_t_timestamp(h_timestamp, t_timestamp):
    """To Compare the time stamps of 2 features 

    Args:
        h_timestamp (UNIX Timestamp): Humidity Timestamp
        t_timestamp (Unix Timestamp): Temperature Timestamp
    """
    h_tobject = unix_timestamp_decode(h_timestamp)
    t_tobject = unix_timestamp_decode(t_timestamp)

    # Calculate the absolute time difference in seconds - for tolerance purpsoe
    time_difference = abs((h_tobject - t_tobject).total_seconds())

    # Check if they have the same date and time (hour and minute)
    if (h_tobject.date() == t_tobject.date()
        and h_tobject.hour == t_tobject.hour
        and h_tobject.minute == t_tobject.minute
        and time_difference <= 10
        ):
        return True
    else:
        return False
    