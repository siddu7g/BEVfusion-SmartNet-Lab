import numpy as np
import cv2
import torch


# Color map for BEV segmentation classes (edit as you like)
COLORMAP = np.array([
    [0, 0, 0],         # background
    [255, 0, 0],       # vehicle
    [0, 255, 0],       # pedestrian
    [0, 0, 255],       # drivable surface
    [255, 255, 0],     # traffic cones
    [255, 0, 255],     # lane lines
    [0, 255, 255],     # others
], dtype=np.uint8)


def bev_to_rgb(bev_pred):
    """
    Convert a 2D BEV segmentation prediction (HxW)
    into an RGB image using the color map above.
    """
    h, w = bev_pred.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)

    for cls_id in range(len(COLORMAP)):
        mask = bev_pred == cls_id
        rgb[mask] = COLORMAP[cls_id]

    return rgb


def visualize_bev(bev_pred, save_path=None, window_name="BEV Visualization"):
    """
    Display or save the BEV segmentation map.
    """
    bev_rgb = bev_to_rgb(bev_pred)

    if save_path:
        cv2.imwrite(save_path, bev_rgb[:, :, ::-1])  # RGB → BGR
    else:
        cv2.imshow(window_name, bev_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return bev_rgb
