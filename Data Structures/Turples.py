# 1. Creating a tuple of colors
colors = ("red", "green", "blue", "yellow", "purple")
print("Initial tuple of colors:", colors)

# 2. Accessing an element by its index
second_color = colors[1]
print("The second color in the tuple is:", second_color)

# 3. Slicing the tuple to get the first three colors
first_three_colors = colors[:3]
print("The first three colors are:", first_three_colors)

# 4. Checking if an element exists in the tuple
is_blue_in_colors = "blue" in colors
print("Is 'blue' in the colors tuple?", is_blue_in_colors)

# 5. Finding the length of the tuple
tuple_length = len(colors)
print("The number of colors in the tuple is:", tuple_length)

# 6. Counting occurrences of an element
blue_count = colors.count("blue")
print("The count of 'blue' in the tuple is:", blue_count)

# 7. Finding the index of an element
yellow_index = colors.index("yellow")
print("The index of 'yellow' in the tuple is:", yellow_index)

# 8. Looping through each color in the tuple
print("All colors in the tuple:")
for color in colors:
    print(color)