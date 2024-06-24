"""
Use a recursive algorithm to fill in an image in the form of a nested list where each inner list is a new row. 

All images will be rectangular (height and width will be the same throughout.)

for example an image that would be printed to the screen like:

    ....####################....
    ....#..................#....
    ....#..................#....
    ....#..................#....
    ....#..................#....
    ....#..................#....
    ....####################....

would be in this format:

image = [
            list('....####################....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....####################....'), 
        ]


The result of the flood fill should be returned as a nested list where any '.' enclosed inside of the '#' should be 'o'

image = [
            list('....####################....'),
            list('....#oooooooooooooooooo#....'),
            list('....#oooooooooooooooooo#....'),
            list('....#oooooooooooooooooo#....'),
            list('....#oooooooooooooooooo#....'),
            list('....#oooooooooooooooooo#....'),
            list('....####################....'), 
        ]

"""

image = [
            list('....####################....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....#..................#....'),
            list('....####################....'), 
        ]

import sys, time


def print_image(im):
   
    for y in range(len(im)):
        for x in range(len(im[0])):
            sys.stdout.write(im[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


def flood_fill(
        image: list, 
        x: int, 
        y: int, 
        new_char: str, 
        old_char: str = None,
        height: int = None,
        width: int = None, 
    ):

    # Programatically determines the height, width, and old_char
    # if it wasn't included in the function arguments
    if height is None:
        height, width = len(image), len(image[0])
    if old_char == None:
        old_char = image[y][x]
    
    if old_char == new_char or image[y][x] != old_char:
        return
    
    image[y][x] = new_char
    print_image(image)
    time.sleep(1)


    # Changes the neighboring characters
    if y + 1 < height and image[y + 1][x] == old_char:
        flood_fill(image, x, y + 1, new_char, old_char, height, width)
    if y - 1 >= 0 and image[y - 1][x] == old_char:
        flood_fill(image, x, y - 1, new_char, old_char, height, width)
    if x + 1 < width and image[y][x + 1] == old_char:
        flood_fill(image, x + 1, y, new_char, old_char, height, width)
    if x - 1 >= 0 and image[y][x - 1] == old_char:
        flood_fill(image, x - 1, y, new_char, old_char, height, width)
    return


print_image(image)
flood_fill(image, 6, 6, 'X')
print_image(image)


