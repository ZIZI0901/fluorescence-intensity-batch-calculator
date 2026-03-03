# Batch Fluorescence Image Intensity Calculator

In experimental research across fields such as physics and biology, fluorescence image grayscale values are commonly used to quantify light intensity for subsequent data analysis. However, general-purpose image processing software can be inefficient and cumbersome when handling large batches of images.

This tool was developed to enable fast, automated batch calculation of fluorescence image intensity values with standardized result export. Users only need to specify the image folder path and set the required parameters. The program will automatically process all images in the folder and generate a well-formatted Excel file for further statistical analysis and visualization.

---

## Usage

### 1. Prepare Image Data

Place all fluorescence images to be analyzed (JPG format supported) into the same folder.

### 2. Select Image Directory

After launching the program, select or enter the folder path containing the images.

### 3. Set Intensity Threshold

Enter a grayscale threshold value.
The program will calculate only the pixels with grayscale values **greater than** the specified threshold. This helps eliminate background noise or non-specific signals.

### 4. Run Batch Processing

Click the **“Process Images”** button.
The program will automatically iterate through all images in the folder, calculate intensity values, and export the results as an Excel file upon completion.

---

## Output Description

The generated Excel file contains the following fields for quantitative comparison and analysis:

* **Image Name**
  The filename of the corresponding image (without file extension), allowing easy data traceability.

* **Maximum Intensity**
  The maximum grayscale value among all pixels in a single image, representing the peak fluorescence signal.

* **Total Intensity**
  The sum of grayscale values for all pixels **above the specified threshold**, representing the overall fluorescence intensity of the target region.

* **Average Intensity**
  The total intensity divided by the total number of pixels in the image (i.e., image resolution; for example, 1920 × 1080 equals the total pixel count).
  This normalized value allows comparison of relative brightness across images with different sizes or resolutions.
