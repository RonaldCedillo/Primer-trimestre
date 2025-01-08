from machine import Pin
import network
import espnow
import time


button = Pin(18, Pin.IN, Pin.PULL_UP)  


station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()

espnow_instance = espnow.ESPNow()
espnow_instance.active(True)


peer_mac = b'\xb0\xb2\x1c\xa8K,'  
espnow_instance.add_peer(peer_mac)


estado = 0
ultima_lectura = 0


def handle_button():
    global estado, ultima_lectura
    ahora = time.ticks_ms()

    if button.value() == 0 and (ahora - ultima_lectura) > 200:  
        ultima_lectura = ahora
        estado = (estado + 1) % 2  
        msg = str(estado)  
        espnow_instance.send(peer_mac, msg)  
        print(f"Estado enviado: {msg}")


while True:
    handle_button()
    time.sleep(0.1)
