from make_thin import thinning
import cv2
import numpy as np

from check import make_1_angle, make_3_angle


def find_end(img):
    # convert all ones (black pixels) to zeroes, and all zeroes (white pixels) to ones
    im = cv2.imread(img, 0)
    thinned_thresh = thinning(im)
    thresh = (thinned_thresh == 0).astype(np.uint8)

    c = make_3_angle(thresh)
    b = make_1_angle(thresh)

    f = b.copy()

    # convert ones to 255 (white)
    thresh *= 255
    b *= 255
    c *= 255
    r = np.ndarray((40, 50))
    # convert greyscale to rgb
    color_img = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    m = 0
    n = 0
    for i in range(1, thresh.shape[0] - 24):
        for j in range(1, thresh.shape[1] - 25):
            cnt1 = np.sum(thresh[i][j - 25:j - 1])
            cnt2 = np.sum(thresh[i][j + 1:j + 25])

            if b[i][j] == 0 and cnt1 <= 23 * 255 and cnt2 <= 23 * 255:
                cv2.rectangle(color_img, (j - 3, i - 3), (j + 3, i + 3), (0, 0, 255), 1)
            else:
                f[i][j] = 1

            if c[i][j] == 0:
                f[i][j] = 0
                cv2.rectangle(color_img, (j - 3, i - 3), (j + 3, i + 3), (255, 0, 0), 1)

            if b[i][j] == 0 or c[i][j] == 0:
                if distance(i, j, m, n) <= 10:
                    f[i][j] = 1
                    f[m][n] = 1
                m = i
                n = j

    d = f
    f *= 255
    # display original and thinned images

    #  cv2.imshow('original image', color_img)
    #  cv2.imshow('thinned image', thresh)
    #  cv2.imshow('b', f)
    #  cv2.waitKey(0)
    #  cv2.destroyAllWindows()
    return d


def distance(x, y, i, j):
    return np.sqrt((x - i) ** 2 + (y - j) ** 2)
