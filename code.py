import usb_hid
from adafruit_hid.mouse import Mouse
import time
import board
import digitalio

mouse = Mouse(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(5)

mouse.move(y=300)

while True:
    click = 1000
    while click > 0:
        led.value = True
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.01)
        click = click - 1
    led.value = False
    time.sleep(10)
