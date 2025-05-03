from gpiozero import Button
from wakeonlan import send_magic_packet

PIN = 4
BOUNCE_TIME = 0.01
MAC_ADDRESS = '00-00-00-00-00-00'

button = Button(pin=PIN, bounce_time=BOUNCE_TIME)
print('Script running!')
while True:
    button.wait_for_press()
    send_magic_packet(MAC_ADDRESS)
    print('Packet sent.')
    button.wait_for_release()