import serial #cargamos la libreria serial
import time
import cv2
import random

#Conectar a arduino mediante el puerto COM
ser = serial.Serial('COM10', 9600) #inicializamos el puerto de serie a 9600 baud
time.sleep(2) # esperar 2 seg.
print ("[INFO] CONECTADO A ARDUINO")
#Encender camara
cam = cv2.VideoCapture(0)
time.sleep(2) # esperar 2 seg.
print ("[INFO] CAMARA ENCENDIDA")

def tomarFoto():
	j = random.randint(1,21)*5
	nombre = "limon_"+str(j)+".jpeg"
	ret, frame = cam.read()
	cv2.imshow("test", frame)
	time.sleep(2) # esperar 2 seg.
	cv2.imwrite(nombre, frame)

def procesarLimon():
	print("tomando foto")
	tomarFoto()
	print("prediciendo clase..")
	print("enviar orden a arduino..")
	entrada = "a"
	ser.write(entrada.encode())



print ("[INFO] LISTO")
ciclo = 1
while ciclo != 0:
	#Leer valor comando desde arduino.
	ser.flush()

	if len(ser.readline()) > 0:
		print("[INFO] ENTRADA RECIBIDA")
		print(ser.readline())
		procesarLimon()

