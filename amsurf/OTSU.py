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



def OTSU(image_path: str, blur: bool = True, g_sigma: float = 2, 
         clear_border: bool = True, 
         crop: tuple[float, float, float, float] | None = None, 
         plot: bool =False) -> dict:
    """
    Implement OTSU thresholding-based image segmentation
    
    Segmentation workflow based on "Measure fluorescence intensity at the 
    nuclear envelope" example at: 
    https://scikit-image.org/docs/stable/auto_examples/applications/index.html

    Args:
        image_path (str): Path to the image file
        blur (bool, optional): If True, apply a Gaussian blur. Defaults to True.
        g_sigma (float, optional): Standard deviation for Gaussian kernel. 
        Defaults to 2.
        clear_border (bool, optional): If True, remove any segments which touch
        the border of the image or cropped region. Defaults to True.
        crop (tuple[float, float, float, float] | None, optional): If not None, 
        crops the input image to the region defined by tuple. The box is a 
        4-tuple defining the left, upper, right, and lower pixel coordinate.
        Defaults to None.
        plot (bool, optional): _description_. Defaults to False.

    Returns:
       dict: region properties including label, centroid, area, and
       equivalent_diameter_area
    """
    
    # load image as grayscale
    img = Image.open(image_path).convert("L")

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
    # path_to_image_LPE0 = "data/project_sharepoint/02_Sample01__GL_concave/01_SEM_maps/20240724_LPE00_ArmSample_001_SESI.tif"
    # regions_LPE0 = OTSU(path_to_image_LPE0, blur=False, g_sigma=2, clear_border=True, crop=[0,0,2048,1400], plot=True)
    # pd.DataFrame(regions_LPE0).to_csv("data/processed/test_LPE0.csv")
    
    path_to_image_CAM1 = "data/project_sharepoint/04_Sample03_IA_flat/20250502_IA_CCAM_M5/Acquisition_08.tif"
    regions_CAM1 = OTSU(path_to_image_CAM1, blur=False, g_sigma=2, clear_border=False, crop=None, plot=True)
    
    plt.show()

    
    