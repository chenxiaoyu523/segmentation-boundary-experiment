# segmentation-boundary-experiment

This code is to find pixels at the object boundary in labelmap and then dilate the boundary for the segmentation-boundary-experiment.
The dilation operate is based on APIs from OpenCV.

## Generating boundary labels

change the root paths and dilation kernel size and run:

'''
python findCountour.py
'''

## Computing mIoU and pixels accuracy

change the root paths and run:

'''
python miou.py
'''

## Examples
<img src="examples/image.png" width = "204" height = "102" div align=left />
<img src="examples/label_color.png" width = "204" height = "102" div align=center />
<img src="examples/label.png" width = "204" height = "102" div align=right />

<img src="examples/dilated_1.png" width = "204" height = "102" div align=left />
<img src="examples/dilated_5.png" width = "204" height = "102" div align=center />
<img src="examples/dilated_10.png" width = "204" height = "102" div align=right />
