import colorgram

colors = colorgram.extract('Hirst_Dots.jpg', 100)
# print(colors)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
