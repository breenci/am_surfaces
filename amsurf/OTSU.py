import numpy as np
import matplotlib.pyplot as plt
import skimage as ski
from PIL import Image
from scipy import ndimage as ndi
import pandas as pd

Image.MAX_IMAGE_PIXELS = 350998111

def plot_label_image(label_image, underlay_image=None):
    """Plot the label image with optional underlay image"""
    
    label_image = ski.color.label2rgb(label_image, image=underlay_image)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(label_image)



def OTSU(image_path, blur=True, g_sigma=2, clear_border=True, crop=None, plot=False):
    
    img = Image.open(image_path)

    # crop image if specified
    if crop is not None:
        img = img.crop(crop)
    
    img_arr = np.array(img)
    
    # apply gaussian blur if required
    if blur:
        img_arr = ski.filters.gaussian(img_arr, sigma=g_sigma)
    
    # apply OTSU thresholding
    threshold = ski.filters.threshold_otsu(img_arr)
    binary = img_arr < threshold
    
    # fill holes
    binary = ndi.binary_fill_holes(binary)
    
    # clear border if required
    if clear_border:
        binary = ski.segmentation.clear_border(binary)
        
    # label the image
    label = ski.measure.label(binary)
    
    # region properties
    regions = ski.measure.regionprops_table(label, 
                                            properties=('label', 'centroid', 'area', 
                                                        'equivalent_diameter_area'))

    # plot the image if required
    if plot:
        plot_label_image(label, underlay_image=img_arr)
    
    return regions
    
if __name__ == "__main__":
    path_to_image_LPE0 = "data/project_sharepoint/02_Sample01__GL_concave/01_SEM_maps/20240724_LPE00_ArmSample_001_SESI.tif"
    regions_LPE0 = OTSU(path_to_image_LPE0, blur=True, g_sigma=2, clear_border=True, crop=[0,0,2048,1400], plot=True)
    pd.DataFrame(regions_LPE0).to_csv("data/processed/test_LPE0.csv")
    
    path_to_image_CAM1 = "data/project_sharepoint/02_Sample01__GL_concave/01_SEM_maps/20241210_CAM01_Site3_SESI_Map.tif"
    regions_CAM1 = OTSU(path_to_image_CAM1, blur=True, g_sigma=2, clear_border=True, crop=[4000, 4000, 8000, 8000], plot=True)
    
    plt.show()

    
    