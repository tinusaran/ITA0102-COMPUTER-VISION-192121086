import cv2 as cv
image=cv.imread("D:\SEM 6\Comp_vision\Programs\Sample_Images\Sample3.jpg")
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
img_gauss=cv.GaussianBlur(gray,(3,3),0)
img_sobelx = cv.Sobel(img_gauss,cv.CV_8U,1,0,ksize=5) 
img_sobely = cv.Sobel(img_gauss,cv.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely
cv.imwrite("Output14_SobelX.jpg",img_sobelx)
cv.imwrite("Output14_SobelY.jpg",img_sobely)
cv.imwrite("Output_Sobel.jpg",img_sobel)
cv.waitkey(0)
cv.destroyAllwindows()
