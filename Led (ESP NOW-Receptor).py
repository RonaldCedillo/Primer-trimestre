import network
import espnow
import machine

S = network.WLAN(network.STA_IF)
S.active(True)
S.disconnect()

E = espnow.ESPNow()
E.active(True)

l1 = machine.Pin(13, machine.Pin.OUT)

while True:
    host, msg = E.recv() 
    if msg:  
        if msg == b'led0n':
            print("led encendido")
            l1.on()
        elif msg == b'led0off':  
            print("led apagado")
            l1.off()
        else:
            print(f"Mensaje desconocido {msg}")
