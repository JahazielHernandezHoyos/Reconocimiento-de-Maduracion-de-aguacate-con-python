# cv2 libreria para el reconcimiento de imagenes
import cv2 

#numpy libreria para crear vectores soportes y matrices y en este caso un arreglo RGB del rango
import numpy as np

#capturadora y 0 representa el numero de la camara que se usara en este caso la principal
cap = cv2.VideoCapture(0)

#rango de colores pantalla maskVerde1
verdeBajo1 = np.array([129, 180, 113], np.uint8)
verdeAlto1 = np.array([180, 255, 160], np.uint8)

#rango de colores pantalla maskVerde2
verdeBajo2=np.array([129, 180, 113], np.uint8)
verdeAlto2=np.array([180, 255, 160], np.uint8)

#while de capturadora
while True:
  ret,frame = cap.read()
  if ret==True:
    #Se convierte de BGR2 a RGB para facilidad en la seleccion del rango de colores
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Se define el rango de la primera pantalla
    maskVerde1 = cv2.inRange(frameHSV, verdeBajo1, verdeAlto1)

    #Se define el rango de la segunda pantalla
    maskVerde2 = cv2.inRange(frameHSV, verdeBajo2, verdeAlto2)

    #Se muestran los rangos
    maskVerde = cv2.add(maskVerde1, maskVerde2)
    maskVerdevis = cv2.bitwise_and(frame, frame, mask= maskVerde)   

    #Se visualizan los fotogramas y el filtro en fotogramas     
    cv2.imshow('frame', frame)
    cv2.imshow('maskRed', maskVerde)
    cv2.imshow('maskRedvis', maskVerdevis)

    #condicional que rompe el bucle para cerrar el programa con (q)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()