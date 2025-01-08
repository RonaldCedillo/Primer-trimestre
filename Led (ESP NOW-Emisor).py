import network
import espnow
import machine
import time


S = network.WLAN(network.STA_IF)
S.active(True)


E = espnow.ESPNow()
E.active(True)


peer_mac = b'\xb0\xb2\x1c\xa8K,' 
E.add_peer(peer_mac)


button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)  


prev_state = button.value()

while True:
    current_state = button.value()
    if current_state != prev_state:  
        if not current_state:  
            E.send(peer_mac, b'led0n')  
            print("Enviado: led0n")
        else:  
            E.send(peer_mac, b'led0off')  
            print("Enviado: led0off")
        prev_state = current_state  

    time.sleep(0.1)  
