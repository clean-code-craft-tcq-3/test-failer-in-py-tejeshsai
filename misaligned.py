
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            assert(get_pair_number_from_color(major, minor) == i*5+j)
            print(f'{i * 5 + j+1:<2} | {major:<6} | {minor:<6}')
    return len(major_colors) * len(minor_colors)


def get_pair_number_from_color(major_color, minor_color):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    try:
        major_index = major_colors.index(major_color)
    except ValueError:
        raise Exception('Could not find major color')
    try:
        minor_index = minor_colors.index(minor_color)
    except ValueError:
        raise Exception('Could not find minor color')
    return major_index * len(minor_colors) + minor_index + 1


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
