import numpy as np
from PIL import Image, ImageDraw

# Load the .npy file
matrix = np.load('ds/g-66-236.npy')
matrix2 = np.load('ds/a-66-236.npy')

print(matrix)

# Define the size of the grid
grid_size = 6
cell_size = 50  # Size of each cell in the grid
circle_radius = 15  # Radius of the circles

# Create an image with a white background
img_size = grid_size * cell_size
img = Image.new('RGB', (img_size, img_size), 'white')
draw = ImageDraw.Draw(img)

# Define colors for the numbers
colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'purple'
}

# Draw the grid
for i in range(grid_size):
    for j in range(grid_size):
        x0 = j * cell_size
        y0 = i * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        draw.rectangle([x0, y0, x1, y1], outline='black')

        # Draw a circle if the matrix value is not 0
        value = matrix[i, j]
        if value != 0:
            # Default to black if color not found
            color = colors.get(value, 'black')
            circle_x = x0 + cell_size // 2
            circle_y = y0 + cell_size // 2
            draw.ellipse(
                [circle_x - circle_radius, circle_y - circle_radius,
                 circle_x + circle_radius, circle_y + circle_radius],
                fill=color
            )
        else:
            color = "black"
            circle_x = x0 + cell_size // 2
            circle_y = y0 + cell_size // 2
            draw.ellipse(
                [circle_x - circle_radius, circle_y - circle_radius,
                 circle_x + circle_radius, circle_y + circle_radius],
                fill=color
            )

img.show()
