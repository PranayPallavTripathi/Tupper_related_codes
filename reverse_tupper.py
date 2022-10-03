import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10
 
# This sets the margin between each cell
MARGIN = 1
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(17):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(106):
        grid[row].append(0)  # Append a cell
 
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1167, 188]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Draw your image and hit the close button when you're done to close this window and get the suitable range of y coordinate printed on the terminal")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Change the colour of that location
            grid[row][column] = 1 - grid[row][column]
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(17):
        for column in range(106):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

N = ''
for column in range(106):
    for row in range(17):
        if grid[16-row][column] == 1:
            N = '1' + N
        elif grid[16-row][column] == 0:
            N = '0' + N
N = int(N, base=2) * 17
print("\nThe range of y in tupper's formula for the submitted figure is given by: N < y < N + 17 where N is \n")
print(N)
