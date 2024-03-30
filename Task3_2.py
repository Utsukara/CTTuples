
# Apply loops and tuples to track and report on event attendance.

# Problem Statement:
# Your goal is to manage an attendance system for various events. 
# Each attendee's data is stored as a tuple containing their name and the event they attended.

# Develop a function to list all attendees of a specific event.
# Implement a feature to count the number of attendees for each event.
# Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
]

def event_attendees(event):
    event_list = [attendee[0] for attendee in attendees if attendee[1] == event]
    if not event_list:
        print(f"No-one attended {event}")
    else:
        print(f"{event}:")
        for person in event_list:
            print(f"- {person} attended this event")


def attendee_count():
    count_dict = {}
    for _, event in attendees:
        if event in count_dict:
            count_dict[event] += 1
        else:
            count_dict[event] = 1
    
    for event, count in count_dict.items():
        print(f"{event}: {count} attendee(s)")

event_attendees("Python Conference")
attendee_count()
