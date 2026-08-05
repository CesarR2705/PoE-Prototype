from rpi_ws281x import PixelStrip, Color
import time

LED_COUNT = 30
LED_PIN = 18
LED_BRIGHTNESS = 70

strip = PixelStrip(
    LED_COUNT,
    LED_PIN,
    brightness=LED_BRIGHTNESS
)

strip.begin()

def set_color(color):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()

try:
    while True:
        print("RED")
        set_color(Color(255, 0, 0))
        time.sleep(2)

        print("GREEN")
        set_color(Color(0, 255, 0))
        time.sleep(2)

        print("BLUE")
        set_color(Color(0, 0, 255))
        time.sleep(2)

        print("WHITE")
        set_color(Color(255, 255, 255))
        time.sleep(2)

        print("OFF")
        set_color(Color(0, 0, 0))
        time.sleep(1)

except KeyboardInterrupt:
    set_color(Color(0, 0, 0))
