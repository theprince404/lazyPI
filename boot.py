import usb_hid
import supervisor

# Define os USB descriptors — O PICO VAI SE APRESENTAR COMO ISSO:
supervisor.set_usb_identification(
    manufacturer="Logitech",          # ← MENTIRA
    product="USB Keyboard",           # ← MENTIRA  
    vid=0x046D,                       # ← VID da Logitech
    pid=0xC31C,                       # ← PID do teclado K120
)

# Habilita HID (Human Interface Device = teclado/mouse)
usb_hid.enable((usb_hid.Device.KEYBOARD,))