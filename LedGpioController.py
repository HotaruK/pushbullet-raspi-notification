import RPi.GPIO as GPIO
from time import sleep


class Color():
    RED = [False, True, True]
    BLUE = [True, False, True]
    GREEN = [True, True, False]
    YELLOW = [False, True, False]
    PURPLE = [False, False, True]
    TEAL = [True, False, False]
    WHITE = [False, False, False]
    OFF = [True, True, True]


class LEDGPIOController():
    def __init__(self, red: int, blue: int, green: int):
        self.red_pin = red
        self.blue_pin = blue
        self.green_pin = green

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)

        GPIO.output(self.red_pin, True)
        GPIO.output(self.blue_pin, True)
        GPIO.output(self.green_pin, True)

    def change_color(self, color: [bool]):
        GPIO.output(self.red_pin, color[0])
        GPIO.output(self.blue_pin, color[1])
        GPIO.output(self.green_pin, color[2])


def light_normal_notify(gpio: LEDGPIOController, color: [bool], cycle=5):
    for i in range(cycle):
        gpio.change_color(color)
        sleep(1)
        gpio.change_color(Color.OFF)
        sleep(1)


def gpio_clean_up():
    GPIO.cleanup()
