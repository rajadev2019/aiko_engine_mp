# Standalone Aiko demo: LED color cycle + hall sensor on serial console.
print("### Aiko Engine MP demo ###")

import esp32
import aiko.event as event
import aiko.led as led

led.initialise()

import applications.default as demo_app

demo_app.initialise()

print("LED: color cycle on 8 pixels @ GPIO 13")
print("Serial: hall sensor every 1s — pass a magnet near the ESP32")


def hall():
    print("Hall sensor:", esp32.hall_sensor())


event.add_timer_handler(hall, 1000, immediate=True)
event.loop()
