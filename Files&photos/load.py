import cv2


def loading(img):
    for i in range(1, img.shape[0] - 24):
        for j in range(1, img.shape[1] - 25):
            if img[i][j] == 0:
                cv2.rectangle(img, (j - 3, i - 3), (j + 3, i + 3), (0, 0, 255), 1)

    #  cv2.imshow('original image', color_img)
    #  cv2.imshow('thinned image', thresh)
    #  cv2.imshow('b', f)
    #  cv2.waitKey(0)
    #  cv2.destroyAllWindows()
    return img
