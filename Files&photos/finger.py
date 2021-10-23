# -*- coding: utf-8 -*-
"""
@author: Rasoul & Sina
"""

import cv2
import numpy as np
from find import find_end
import winsound
from matching import matching
from load import loading


def process(address):
    k = find_end(address)
    return k


def comp(address1, address2):
    im1 = process(address1)
    im2 = process(address2)
    count = max(im1.size - np.count_nonzero(im1), im2.size - np.count_nonzero(im2))
    equal = matching(im1, im2)

    #  print(f'{count},  {equal}')
    if equal / count >= 0.5:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        return 1
    else:
        return 0

    ############################ load #######################################
    #  img = cv2.cvtColor(im1, cv2.COLOR_GRAY2RGB)
    #  for i in range(1, img.shape[0] - 20):
    #    for j in range(1, img.shape[1] - 20):
    #        if im1[i][j] == 0:
    #            cv2.rectangle(img, (j - 3, i - 3), (j + 3, i + 3), (0, 0, 255), 1)
    #        if im2[i][j] == 0:
    #            cv2.circle(img,(j, i), 3, (255, 0, 0))
    #  cv2.imshow('h', img)
    #  v2.waitKey(0)
    #  cv2.destroyAllWindows()
    ####################################################################


if __name__ == "__main__":
    try:
        comp('C:/Users/SAHAND/Desktop/ap/b1.png', 'C:/Users/SAHAND/Desktop/ap/a.png')
    except:
        raise
