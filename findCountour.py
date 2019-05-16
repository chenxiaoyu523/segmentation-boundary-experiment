#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# define the dilation kernel size
k = 4
saveroot = '4/'

def get_border(label):
    h, w = label.shape
    padded = np.ones([h+2, w+2])
    padded[1:-1, 1:-1] = label

    m00 = padded[0:-2, 0:-2]
    m01 = padded[0:-2, 1:-1]
    m02 = padded[0:-2, 2:]
    m11 = padded[1:-1, 0:-2]
    m12 = padded[1:-1, 1:-1]
    m13 = padded[1:-1, 2:]
    m21 = padded[2:, 0:-2]
    m22 = padded[2:, 1:-1]
    m23 = padded[2:, 2:]

    sums = m00+m01+m02+m11+m12+m13+m21+m22+m23

    border = sums == (9*label)

    return border

if __name__ == "__main__":
    iters = 0
    for root, dirs, files in os.walk("val", topdown=False):
        for name in files:
            ext = name.split('_')[-1]
            if ext == 'labelTrainIds.png':
                lbpath = os.path.join(root, name)
                savepath = os.path.join(saveroot, name)
                lb = cv2.imread(lbpath, cv2.IMREAD_UNCHANGED).astype(np.long)
                border = get_border(lb)

                kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(k, k))
                border = cv2.erode(255*border.astype(np.uint8),kernel)

                border = np.clip((lb+border),0,255)

                cv2.imwrite(savepath, border)
                iters = iters+1
                print(iters, k)




