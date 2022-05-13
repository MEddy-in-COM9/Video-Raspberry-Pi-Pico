import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
bottone = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    lled = bottone.value()
    led.value(lled)