# Minimal MicroPython demo (no Wi-Fi): LED cycle + hall sensor on serial.
from machine import Pin
from neopixel import NeoPixel
import esp32
import time

print("### Aiko Engine MP — standalone demo ###")
print("GPIO 13: 8-pixel color cycle | Serial: hall sensor every 1s")

PIXEL_PIN = 13
PIXEL_COUNT = 8
COLORS = ((48, 0, 0), (0, 48, 0), (0, 0, 48), (48, 48, 0), (48, 0, 48), (48, 48, 48))

strip = NeoPixel(Pin(PIXEL_PIN), PIXEL_COUNT)
index = 0
next_color = time.ticks_ms() + 1000

while True:
    color = COLORS[index % len(COLORS)]
    for i in range(PIXEL_COUNT):
        strip[i] = color
    strip.write()

    if time.ticks_diff(time.ticks_ms(), next_color) >= 0:
        index += 1
        next_color = time.ticks_add(time.ticks_ms(), 1000)
        print("Hall sensor:", esp32.hall_sensor(), "| color:", index % len(COLORS))

    time.sleep_ms(50)
