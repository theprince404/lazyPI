import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Espera o Windows reconhecer

kbd = Keyboard(usb_hid.devices)

# Digita o comando
for char in "sudo apt update && sudo apt full-upgrade &&  sudo apt autoclean":
    if char == " ":
        kbd.send(Keycode.SPACEBAR)
    elif char == "&":
        kbd.send(Keycode.SHIFT, Keycode.SEVEN)
    elif char == "-":
        kbd.send(Keycode.MINUS)
    else:
        kbd.send(getattr(Keycode, char.upper()))
        time.sleep(0.02)

kbd.send(Keycode.ENTER)
