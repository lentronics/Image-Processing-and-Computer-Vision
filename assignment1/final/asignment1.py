import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
from matplotlib import pyplot as plt

#name of image
filename = 'coins1.png'
#array to store details of the image
filenamearray = filename.split('.')

img = cv2.imread(filename) #gets image and greyscales it
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #can be used to greyscale image if the original is grabbed above

#kernels for sobel
#horizontal
kernel = np.matrix([[-1,0,1],[-2,0,2],[-1,0,1]])
#vertical
kernel2 = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])

#applies kernels to the image
#uses a 64 bit color space to avoid loosing negatives
img_horizontal = cv2.filter2D(img_grey,cv2.CV_64F,kernel)
img_vertical= cv2.filter2D(img_grey,cv2.CV_64F,kernel2)
img_magnitude = abs(img_horizontal) + abs(img_vertical)
img_mag,img_angle = cv2.cartToPolar(img_horizontal,img_vertical) #uses the x and y sobel to calculate the orientation

#sets up the window for displaying the images and cmaps

plt.subplot(3,3,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,4),plt.imshow(img_grey,cmap = 'gray')
plt.title('greyscale'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3),plt.imshow(img_magnitude,cmap = 'gray')
plt.title('magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,6),plt.imshow(img_angle,cmap = 'gray')
plt.title('angle'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,2),plt.imshow(img_horizontal,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5),plt.imshow(img_vertical,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


#plt.subplot(3,3,7),plt.hist(img_angle, 50, normed=1, facecolor='g', alpha=0.75)
img_array=[]
for i in range(0,len(img_angle)):
	for j in range(0,len(img_angle[0])):
		img_array.append(img_angle[i][j])

plt.subplot(3,3,7),plt.hist(img_array) #creates a histogram of the angles

#displays the result
plt.show()

#cv2.suptitle('test')

#generates a name for the files to be saved
finalfilename = filenamearray[0] + '_sobel_magnitude' + '.' + filenamearray[1]
finalfilename2 = filenamearray[0] + '_sobel_angle' + '.' + 'txt'

#saves the file
plt.imshow(img_magnitude,cmap = 'gray'),plt.xticks([]), plt.yticks([])
#plt.show()
plt.savefig(finalfilename)

# file = open(finalfilename2, 'w+')
# file.write(img_angle)
# file.close()