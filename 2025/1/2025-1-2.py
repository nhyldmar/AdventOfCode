"""https://adventofcode.com/2025/day/1 Part 2"""

dial_state = 50
zero_count = 0
sequence = []

# Extract
with open("2025/1/input.txt") as file:
    lines = file.readlines()

for line in lines:
    # Parse
    direction = line[0]
    num = int(line[1:])

    # Handle
    if direction == "L":
        sequence.extend([-1 for _ in range(num)])
    elif direction == "R":
        sequence.extend([1 for _ in range(num)])

# Count
for tick in sequence:
    dial_state += tick
    dial_state %= 100
    if dial_state == 0:
        zero_count += 1

print(zero_count)
