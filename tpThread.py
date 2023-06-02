import threading
import time

#Esta función es la que se ejecutará cuando llame a start. Muestra el nombre y el id
def imprimir():
    i = 0;
    while (i<5):
        print(f'{threading.current_thread().name} {threading.get_native_id()}')
        i = i+1
        time.sleep(1)

# creamos los hilos
hilo1 = threading.Thread(target=imprimir)
hilo2 = threading.Thread(target=imprimir)
hilo3 = threading.Thread(target=imprimir)

# ejecutamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()


# el programa principal sigue ejecutándose aunque los hilos no hayan terminado
print(f'{threading.current_thread().name} {threading.get_native_id()}')