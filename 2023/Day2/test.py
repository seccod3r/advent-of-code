import sys
from collections import defaultdict
# Read input file and initialize variables
data = open(sys.argv[1]).read().strip()
total_points = 0
cumulative_score = 0
# Iterate through each line in the input data
for line in data.split('\n'):
    valid_config = True
    identifier, events = line.split(':')
    color_counts = defaultdict(int)
    # Process each event in the line
    for event in events.split(';'):
        for ball_info in event.split(','):
            count, color = ball_info.split()
            count = int(count)
            color_counts[color] = max(color_counts[color], count)
            # Check if count exceeds specified limits
            if count > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                valid_config = False
    # Calculate the score for the current line
    score = 1
    for count in color_counts.values():
        score *= count
    cumulative_score += score
    # Add identifier to total points if the configuration is valid
    if valid_config:
        total_points += int(identifier.split()[-1])
# Print the results
print(total_points)
print(cumulative_score)