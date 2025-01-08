from machine import I2C, Pin
from i2c_lcd import I2cLcd
import network
import espnow
import time


i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd_address = 0x27 
lcd = I2cLcd(i2c, lcd_address, 2, 16)


lcd.backlight_on()
lcd.clear()
lcd.putstr("Esperando mensajes...")


station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()

espnow_instance = espnow.ESPNow()
espnow_instance.active(True)


textos = ["Adonis   Paredes", "Brian    Aucapiña"]


def desplazar_der_a_izq(texto):
    texto_expandido = " " * 16 + texto  
    for i in range(len(texto_expandido) - 15):  
        lcd.clear()
        lcd.putstr(texto_expandido[-(i + 16):-i or None])  
        time.sleep(0.3)  


while True:
    host, msg = espnow_instance.recv()  

    if msg:
        estado = int(msg.decode())  
        print(f"Estado recibido: {estado}")

        if estado == 1:  
            lcd.clear()
            
            while True:  
                desplazar_der_a_izq(textos[0])  
                desplazar_der_a_izq(textos[1])  
