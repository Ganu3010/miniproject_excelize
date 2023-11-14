import cv2 as cv
import easyocr
import os
# import matplotlib.pyplot as plt

reader = easyocr.Reader(['en'])
filePath = 'test_data/'

for image in os.listdir(filePath):
    img = cv.imread(filePath+image)


    result = reader.readtext(img)

# cv.imshow(img)

    for res in result:
        xy = res[0]
        xy1, xy2, xy3, xy4 = xy[0], xy[1], xy[2], xy[3]
        det, conf = res[1], res[2]

        cv.rectangle(img, pt1 = (int(xy1[0]), int(xy1[1])), pt2 = (int(xy3[0]), int(xy3[1])), color=(255, 0, 0), thickness=1)
    
        cv.putText(img, text = '{}'.format(round(conf, 2)), org=(int(xy3[0]), int(xy3[1])), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=1)
        print("Text found: ", det)

    cv.imshow(image, img)

cv.waitKey(0)