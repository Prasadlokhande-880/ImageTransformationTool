# Image Transformation Script  

This project demonstrates various **image transformation techniques** using **OpenCV** and **NumPy**, suitable for image processing tasks like data augmentation, visual effects, and preprocessing.  

---

## **Features**  
1. **Image Shifting**  
   - Translates the image by modifying pixel positions based on specified x and y offsets.  
   - Achieved using affine transformation matrices.  

2. **Image Resizing**  
   - Adjusts the image dimensions proportionally using specified scaling factors for width and height.  
   - Uses interpolation for smooth resizing.  

3. **Image Rotation**  
   - Rotates the image around its center by a given angle.  
   - Includes optional scaling during rotation for resizing.  

4. **Image Skewing**  
   - Applies a shear transformation along the x and y axes, distorting the image in specific directions.  

---

## **Technologies Used**  
- **Python**  
- **OpenCV**: For image manipulation and transformations (`cv2.warpAffine`, `cv2.resize`, `cv2.getRotationMatrix2D`).  
- **NumPy**: For creating and managing affine transformation matrices.  

---

## **Installation**  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo/image-transformations.git  
   ```  

2. Install dependencies:  
   ```bash  
   pip install opencv-python-headless numpy  
   ```  

3. Run the script:  
   ```bash  
   python image_transformations.py  
   ```  

---

## **Usage**  

Replace `"your_image.jpg"` with the path to your image file, and uncomment the desired transformations in the script:  

- **Shift Image**:  
   ```python  
   shifted = shift_image(img, shift_x=50, shift_y=30)  
   ```  

- **Resize Image**:  
   ```python  
   resized = resize_image(img, factor_x=1.5, factor_y=1.2)  
   ```  

- **Rotate Image**:  
   ```python  
   rotated = rotate_image(img, degrees=45)  
   ```  

- **Skew Image**:  
   ```python  
   skewed = skew_image(img, shear_x=0.2, shear_y=0.1)  
   ```  

Display results using OpenCV:  
```python  
cv2.imshow("Transformed Image", transformed_img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
```  

---

## **Topics Covered**  
- Image Shifting, Resizing, Rotating, and Skewing.  
- Affine Transformations for modifying image geometry.  
- Using OpenCV functions like `cv2.warpAffine`, `cv2.resize`, and `cv2.getRotationMatrix2D`.  
- Utilizing NumPy for creating transformation matrices.  

---

## **Contributions**  
Feel free to fork this repository and submit pull requests for additional transformations or optimizations.  

---

## **License**  
This project is licensed under the MIT License.  

--- 

Happy Transforming! 🎉
