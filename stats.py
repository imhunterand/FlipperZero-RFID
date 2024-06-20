import os

def display_stats():
    log_file = 'logs/activity.log'
    if not os.path.exists(log_file):
        print("No activity logs found.")
        return
    
    with open(log_file, 'r') as file:
        logs = file.readlines()

    actions = {}
    for log in logs:
        action = log.split(' - ')[2].split(', ')[0].split(': ')[1]
        if action in actions:
            actions[action] += 1
        else:
            actions[action] = 1
    
    print("\nUsage Statistics:")
    for action, count in actions.items():
        print(f"{action}: {count} times")
