# importe a biblioteca opencv 
import cv2

#Carregue o arquivo do classificador cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# Defina um objeto VideoCapture
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()

    # Converta para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecte os rostos
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Desenhe o retângulo ao redor de cada rosto
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Exiba o quadro resultante
    cv2.imshow('frame', frame)
      
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as telas
cv2.destroyAllWindows()