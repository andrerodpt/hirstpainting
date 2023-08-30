import colorgram

def extract_colors_from_image(nr_of_colors):
    colors = colorgram.extract('image.jpg', nr_of_colors)
    color_stack = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r < 225 and g < 225 and b < 225:
            color_stack.append((r, g, b))
    return color_stack
