import serial #cargamos la libreria serial
import time
import cv2
import random

#Conectar a arduino mediante el puerto COM
ser = serial.Serial('COM10', 115200) #inicializamos el puerto de serie a 9600 baud
time.sleep(2) # esperar 2 seg.

test = True
while test:
	ser.flush()
	val = ser.readline()
	if len(val) > 0:
		print("tomar foto")