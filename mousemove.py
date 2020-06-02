from pynput.mouse import Button, Controller

mouse = Controller()

# show mouse current position
# print ("Current position: " + str(mouse.position))

# set mouse position
# mouse.position = (1285.75, 577.875)

# move mouse to another position
# mouse.move(20, -13)

# click mouse left and right button with number of times
# mouse.click(Button.left, 1)
# mouse.click(Button.right, 1)

# keep press and release button
# mouse.press(Button.left)
# mouse.release(Button.left)

# Scroll up two steps
mouse.scroll(0, 2)

# Scroll right five steps
# mouse.scroll(5, 0)
