# conversion of text to handwriting 

import pywhatkit as kit
import cv2


text = input("Enter your text: ")
kit.text_to_handwriting(text, save_to="txt.png")
img = cv2.imread("txt.png")
cv2.imshow("txt",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


