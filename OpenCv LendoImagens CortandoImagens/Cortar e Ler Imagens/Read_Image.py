import cv2

# Leia a imagem
img = cv2.imread("butterfly.jpg")

# Exiba a imagem colorida
cv2.imshow("Imagem de Exibicao",img)

# Converta a imagem colorida para escala de cinza
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Exiba a imagem em escala de cinza
cv2.imshow("Escala de Cinza", gray_img)


#print(gray_img)

cv2.waitKey(0)
