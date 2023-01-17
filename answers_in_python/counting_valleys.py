"""
An avid hiker keeps meticulous records of their hikes.
During the last hike that took exactly *STEP* steps, for every step
it was noted if it was an uphill, *U*, or a downhill, *D* step.
Hikes always start and end at sea level, and each step up or down
represents a  unit change in altitude. We define the following terms:

- A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.

- A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the
number of valleys walked through.

Link: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

def countingValleys(steps, path):
    initial_step_level = 0
    through_valleys = 0

    for step in path:
        if step == 'U':
            initial_step_level += 1
            if initial_step_level == 0:
                through_valleys += 1
        else:
            initial_step_level -= 1

    return through_valleys