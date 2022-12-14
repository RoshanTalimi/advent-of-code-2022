# Set up a list to keep track of the total Calories carried by each Elf
elf_calories = [6000, 4000, 11000, 24000, 10000]

# Set up a variable to keep track of the current Elf's total Calories
current_total = 0

# Read the input one line at a time
while True:
    # Read the next line of input
    line = input()

    # Check if we've reached the end of the input
    if line == "":
        # Add the current Elf's total Calories to the list
        elf_calories.append(current_total)

        # Reset the current Elf's total Calories
        current_total = 0

        # Move on to the next Elf
        continue

    # Otherwise, add the item's Calories to the current Elf's total
    current_total += int(line)

# Find the Elf carrying the most Calories
max_calories = max(elf_calories)

# Print the number of Calories carried by that Elf
print(max_calories)
