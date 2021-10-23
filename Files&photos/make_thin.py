import cv2
from check import *
import numpy as np


def thinning(img):
    #  img = cv2.imread('a.jpg', 0)
    ret, orig_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    bin_thresh = (orig_thresh == 0).astype(int)
    thinned_thresh = bin_thresh.copy()

    # if the thinned threshold reaches a steady state, we'll break out of the loop
    while 1:
        # make a copy of the thinned threshold array to check for changes
        thresh_copy = thinned_thresh.copy()
        # step one
        pixels_meeting_criteria = []
        # check all pixels except for border and corner pixels
        # if a pixel meets all criteria, add it to pixels_meeting_criteria list
        for i in range(1, thinned_thresh.shape[0] - 1):
            for j in range(1, thinned_thresh.shape[1] - 1):
                if (pixel_is_black(thinned_thresh, i, j) and
                        pixel_has_3_to_8_black_neighbors(thinned_thresh, i, j) and
                        pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                        at_least_one_of_P2_P4_P6_is_white(thinned_thresh, i, j) and
                        at_least_one_of_P4_P6_P8_is_white(thinned_thresh, i, j)):
                    pixels_meeting_criteria.append((i, j))

        # change noted pixels in thinned threshold array to 0 (white)
        for pixel in pixels_meeting_criteria:
            thinned_thresh[pixel] = 0

        # step two
        pixels_meeting_criteria = []
        # check all pixels except for border and corner pixels
        # if a pixel meets all criteria, add it to pixels_meeting_criteria list
        for i in range(1, thinned_thresh.shape[0] - 1):
            for j in range(1, thinned_thresh.shape[1] - 1):
                if (pixel_is_black(thinned_thresh, i, j) and
                        pixel_has_3_to_8_black_neighbors(thinned_thresh, i, j) and
                        pixel_has_1_white_to_black_neighbor_transition(thinned_thresh, i, j) and
                        at_least_one_of_P2_P4_P8_is_white(thinned_thresh, i, j) and
                        at_least_one_of_P2_P6_P8_is_white(thinned_thresh, i, j)):
                    pixels_meeting_criteria.append((i, j))

        # change noted pixels in thinned threshold array to 0 (white)
        for pixel in pixels_meeting_criteria:
            thinned_thresh[pixel] = 0

        # if the latest iteration didn't make any difference, exit loop
        if np.all(thresh_copy == thinned_thresh):
            break
    return thinned_thresh
