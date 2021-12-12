import cv2
import numpy as np

real_img = cv2.imread('spider.jpg')

fake_img = np.ones(real_img.shape, np.uint8) * 255

cv2.imshow('real',real_img)
cv2.imshow('fake', fake_img)
cv2.waitKey()

cv2.destroyAllWindows()

cv2.imwrite('fake.png',fake_img)