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


textos = ["Adonis Paredes", "Brian Aucapina"]


while True:
    host, msg = espnow_instance.recv()  
    
    if msg:
        estado = int(msg.decode())  
        print(f"Estado recibido: {estado}")
        
        lcd.clear()  
        if estado == 0:
            lcd.putstr(textos[0])  
        elif estado == 1:
            lcd.putstr(textos[0])  
            lcd.move_to(0, 1)  
            
            for i in range(1, 11):
                lcd.move_to(0, 1)  
                lcd.putstr(f"Contando: {i}   ")  
                time.sleep(1)  
            
           
            lcd.move_to(0, 1)
            lcd.putstr("                ")  
            lcd.move_to(0, 1)
            lcd.putstr(textos[1])  
