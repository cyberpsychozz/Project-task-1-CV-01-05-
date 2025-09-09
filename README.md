Coin Contour Detection
Overview
This Python script processes a grayscale image of coins from the scikit-image dataset, detects contours of coins using edge detection and morphological operations, filters them by area, and draws the filtered contours on the original image. The result is saved as a PNG file, and the number of detected contours is printed to the console.
Requirements

Python 3.x
Libraries:
numpy: For array operations
opencv-python (cv2): For image processing and contour detection
scikit-image: For loading the test image (coins)



Install dependencies using pip:
pip install numpy opencv-python scikit-image

Usage

Ensure all required libraries are installed.
Run the script:python coins_contour_detection.py


The script will:
Load the coins image from scikit-image.
Apply Canny edge detection, thresholding, and morphological closing.
Detect and filter contours by area (between 200 and 5000 pixels).
Draw green contours on the original image and save it as res.png.
Print the number of detected contours to the console.



Code Explanation

Input: Grayscale coins image from scikit-image (304x400 pixels).
Processing Steps:
Edge Detection: Uses Canny edge detector (thresholds: 50, 150).
Thresholding: Applies Otsu's method for binarization.
Morphological Operation: Performs closing with a 3x3 kernel to reduce noise.
Contour Detection: Finds external contours using OpenCV's findContours.
Filtering: Keeps contours with area between 200 and 5000 pixels.
Visualization: Draws filtered contours in green on the original image.


Output:
res.png: Image with green contours around detected coins.
Console output: Number of filtered contours (e.g., ~27 for the coins image).



Notes

The original code contains a syntax error in the contour filtering loop (incorrect indentation of the if statement). Ensure proper indentation for correct execution.
The input image is grayscale; drawing colored contours requires converting it to BGR format (cv.cvtColor(imgray, cv.COLOR_GRAY2BGR)) for proper color display.
Uncommented cv.imwrite lines can be used for debugging intermediate results (e.g., edges, thresholded image).
Adjust min_area and max_area to fine-tune contour filtering for different images.

Limitations

The script assumes the input image is grayscale and may not handle colored images correctly without modification.
No error handling for cases like empty contour lists or file I/O issues.
Parameters (Canny thresholds, kernel size, area bounds) are tuned for the coins image and may need adjustment for other datasets.

Example Output

Console: Prints the number of detected coins (e.g., 27).
File: res.png with green contours around coins.

License
This project is unlicensed and provided as-is for educational purposes.