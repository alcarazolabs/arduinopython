import serial #cargamos la libreria serial

ser = serial.Serial('COM10', 9600) #inicializamos el puerto de serie a 9600 baud

#variable para almacenar el mensaje
#le asignamos un valor introducido por el usuario
print ("Introduce un caracter ('s' para salir): ")
#leer valor.
entrada = input()
while entrada != 's': #introduciendo 's' salimos del bucle
	#enviar a arduino
	ser.write(entrada.encode())
	print ("He enviado: "+entrada)
	print ("Introduce un caracter ('s' para salir): ")
	entrada = input() #introduce otro caracter por teclado


