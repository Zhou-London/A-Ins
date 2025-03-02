# 520*700
import cv2
import os

for imageName in os.listdir('images'):
    image = cv2.imread(f'images/{imageName}')

    size = image.shape

    width = size[1]
    height = size[0]

    scale = 520 / width
    targetHeight = int(height * scale)

    if width > 520:
        resizedImage = cv2.resize(image, (520, targetHeight), interpolation=cv2.INTER_AREA)
    else:
        resizedImage = cv2.resize(image, (520, targetHeight), interpolation=cv2.INTER_LINEAR)

    if targetHeight > 720:
        cropped = (targetHeight - 720) // 2
        resizedImage = resizedImage[cropped:targetHeight-cropped, : ]

    cv2.imwrite(f'out_{imageName[:-4]}.png', resizedImage)