import cv2

img = cv2.imread("poster.jpg")

rocket = img[120:360,400:500]

img[0:240, 500:600] = rocket

text_to_show = "Eu amo programar na BYJUS FutureSchool"


cv2.putText(img,  
           text_to_show,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.imshow("resultado",img)

###### ATIVIDADE ADICIONAL ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)
