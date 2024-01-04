import numpy as np
import cv2
import matplotlib.pyplot as plt


def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)
    
    
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
    
    
def bounding_box(binary_mask):
    # Get the indices of the non-zero elements
    y_indices, x_indices = np.nonzero(binary_mask)
    # Compute the min and max coordinates for the bounding box
    y_min, y_max = y_indices.min(), y_indices.max()
    x_min, x_max = x_indices.min(), x_indices.max()
    return x_min, y_min, x_max, y_max


def adjust_bbox(box, img_size, margin=0.1):
    ''' img_size = (w, h) '''
    pixel_margin = int(margin * min(img_size))
    new_box = [0, 0, 0, 0]
    new_box[0] = max(0, box[0] - pixel_margin)
    new_box[1] = max(0, box[1] - pixel_margin)
    new_box[2] = min(img_size[0], box[2] + pixel_margin)
    new_box[3] = min(img_size[1], box[3] + pixel_margin)
    return new_box


def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))    
