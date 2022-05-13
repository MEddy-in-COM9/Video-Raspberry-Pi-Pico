import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
pulsante = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    lp = pulsante.value()
    if lp == 1:
        led.value(1)
    else:
       led.value(0)
      
    utime.sleep(0.1)
                       
                       