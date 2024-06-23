import time
import pyautogui
from screeninfo import get_monitors

# Get height and width of the monitor
monitor = get_monitors()[0]
screen_x = monitor.width
screen_y = monitor.height

# Get initial screenshot
screen_img = pyautogui.screenshot()

# While the retry button at the end of a game isnt showing, bot is on.
while ((screen_img.getpixel((0.475 * screen_x,screen_y * 0.75)) != (83,83,83)) | (screen_img.getpixel((0.525 * screen_x,screen_y * 0.75)) != (83,83,83))):
    # Get new screenshot.
    screen_img = pyautogui.screenshot()

    # Checking 25 pixels for obstacle to maximise detection.
    for i in range(25):
        # If low obstacle detected, jump and break (no need to duck check).
        if (screen_img.getpixel((screen_x * 0.19 + (i * 2),screen_y * 0.825)) == (83,83,83)):
            pyautogui.press('up')
            break
        # Else if high obstacle spotted, duck for 2 seconds.
        elif screen_img.getpixel((screen_x * 0.19, screen_y * 0.72)) == (83,83,83):
            pyautogui.press('down')
            time.sleep(2)

