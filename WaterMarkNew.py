import cv2
import numpy as np
original_image = cv2.imread(r'D:\SEM 6\Comp_vision\Programs\Sample_Images\Sample9.jpg')
watermark_text = 'Hahahahahaha'
watermarked_image = original_image.copy()
position = (1500, 1500)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 30
font_color = (250, 0, 0)
font_thickness = 25
cv2.putText(watermarked_image, watermark_text, position, font, font_scale, font_color, font_thickness)
cv2.imwrite('watermarked_image.jpg', watermarked_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()