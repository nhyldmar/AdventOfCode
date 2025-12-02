"""https://adventofcode.com/2025/day/1 Part 1"""

dial_state = 50
zero_count = 0

# Extract
with open("2025/1/input.txt") as file:
    lines = file.readlines()

for line in lines:
    # Parse
    direction = line[0]
    num = int(line[1:])

    # Handle
    if direction == "L":
        dial_state -= num
    elif direction == "R":
        dial_state += num
    dial_state %= 100

    # Count
    if dial_state == 0:
        zero_count += 1

print(zero_count)
