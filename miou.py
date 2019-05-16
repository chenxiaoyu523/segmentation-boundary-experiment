#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
import os.path as osp
import time
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt 
import skimage.morphology as sm

#define image roots
preds_root = 'pspnet/'
label_root = '15'
#cityscapes
n_classes = 19
ignore_idx = 255

#initializing
hist = np.zeros((n_classes, n_classes), dtype=np.float32)
it = 0

#reading paths
f = open('val.txt')
files = f.readlines()

def compute_hist(pred, lb):
    keep = np.logical_not(lb==ignore_idx)
    merge = pred[keep] * n_classes + lb[keep]
    hist = np.bincount(merge, minlength=n_classes**2)
    hist = hist.reshape((n_classes, n_classes))
    return hist

for item in files:
    #counting
    print(it)
    it = it+1

    # reading samples
    item = item.strip()
    preds_path = preds_root + item
    label_path = label_root + item
    preds = cv2.imread(preds_path, cv2.IMREAD_GRAYSCALE).astype(np.int16)
    label = cv2.imread(label_path, cv2.IMREAD_GRAYSCALE).astype(np.int16)

    #computing histograms
    hist_once = compute_hist(preds, label)
    hist = hist + hist_once

#results
acc = np.diag(hist).sum()/hist.sum()
IOUs = np.diag(hist) / (np.sum(hist, axis=0)+np.sum(hist, axis=1)-np.diag(hist))
mIOU = np.mean(IOUs)
print('mIOU', mIOU)
print('pixel_acc', acc)

