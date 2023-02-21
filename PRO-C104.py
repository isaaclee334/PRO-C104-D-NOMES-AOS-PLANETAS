import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sol",
           (100,80),  
           cv2.FONT_HERSHEY_COMPLEX,
           2,
           color=(0,0,255)
           )

cv2.putText(img,  
           "mercurio",
           (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.4,
             color=(0,0,255)
           )

cv2.putText(img,  
           "venus",
           (200,180),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.4,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "terra",
           (290,180),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.4,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "marte",
           (350,180),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.4,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "jupiter",
           (490,80),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "saturno",
           (800,117),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "urano",
           (990,140),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.4,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "netuno",
           (1100,140),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.4,  
           color=(0,0,255)
           )

cv2.imshow("resultado",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)