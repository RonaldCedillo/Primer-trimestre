from machine import I2C, Pin
from i2c_lcd import I2cLcd
import network
import espnow
import time


i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd_address = 0x27  

try:
    lcd = I2cLcd(i2c, lcd_address, 2, 16)
except OSError:
    print("Error: LCD no encontrado en la dirección especificada.")
    raise


lcd.backlight_on()
lcd.clear()
lcd.putstr("Esperando mensajes...")


station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()

espnow_instance = espnow.ESPNow()
espnow_instance.active(True)


while True:
    host, msg = espnow_instance.recv()
    if msg:
        print(f"Mensaje recibido: {msg}")
        lcd.clear()
        textos = msg.decode().split("|")
        if len(textos) >= 2:
            lcd.putstr(textos[0][:16])
            lcd.move_to(0, 1)
            lcd.putstr(textos[1][:16])
        else:
            lcd.putstr("Error en mensaje")
    time.sleep(1)
