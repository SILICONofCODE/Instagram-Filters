import cv2
import matplotlib.pyplot as plt

im=cv2. imread( 'bunny.jpeg' );

dst=cv2.GaussianBlur(im, (7, 7), cv2.BORDER_DEFAULT)
#medianBlur
#dst=cv2.medianBlur(im,5)
#bilateralFilter(im, 15, 80, 80, Core.BORDER_DEFAULT)

'''
edges = cv2. Canny(im,100,300)
plt.imshow(edges)
plt. show( )
'''

plt.imshow(dst)
plt. show( )