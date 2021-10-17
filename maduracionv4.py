import cv2
import numpy as np

def dibujar(mask,color):
  contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    if area > 3000:
      M = cv2.moments(c)
      
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])
      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame,(x,y),7,(0,50,0),-1)
      #cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,0,0),1,cv2.LINE_AA)
      font = cv2.FONT_HERSHEY_SIMPLEX

      if area > 5000:
        print("Hay un aguacate maduro")

      else:
        print("no hay")

      cv2.putText(frame,'Aguacate Maduro', (x+10,y), font, 0.75, (0,0,0), 1,cv2.LINE_AA)
      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
      #print("no hay un aguacate maduro")
        
  

#cap = cv2.VideoCapture("aguacates2.jpg")
cap = cv2.VideoCapture(0)

VerdeBajo = np.array([17,93,82],np.uint8)
VerdeAlto = np.array([60,131,133],np.uint8)


font = cv2.FONT_HERSHEY_SIMPLEX
while True:

  ret,frame = cap.read()

  if ret == True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    maskVerde = cv2.inRange(frameHSV,VerdeBajo,VerdeAlto)
    dibujar(maskVerde,(0,255,0))
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()

