import cv2
import numpy as np
from random import randrange, randint

def draw_triangle(r_image, f_image):
    ''' Draws a triangle randomly in the fake image around a random point selected in the real image'''

    TRIANGLE_SIZE = 15

    img_shape = r_image.shape

    #Get a random point from the real image
    pt = (randrange(img_shape[0]), randrange(img_shape[1]))

    #Get the color of that point and convert it to int
    color = (int(r_image[pt[0], pt[1], 0]),int(r_image[pt[0], pt[1], 1]),int(r_image[pt[0], pt[1], 2]))

    pt1 = (pt[1] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE), pt[0] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE))
    pt2 = (pt[1] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE), pt[0] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE))
    pt3 = (pt[1] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE), pt[0] + randint(-TRIANGLE_SIZE, TRIANGLE_SIZE))

    triangle_pts = np.array([pt1, pt2, pt3])

    #Draw triangle
    cv2.drawContours(fake_img,[triangle_pts], 0, color, -1)

''' Initialize images '''
real_img = cv2.imread('spider.jpg')
fake_img = np.ones(real_img.shape, np.uint8) * 255

for i in range(50000):
    draw_triangle(real_img, fake_img)

cv2.imshow('real',real_img)
cv2.imshow('fake', fake_img)
cv2.waitKey()

cv2.imwrite('fake.png',fake_img)