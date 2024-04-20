import cv2


image_path = r"C:\Users\HP\Downloads\cartez.jpg"  
image = cv2.imread(image_path)


x1, y1 = 195, 254  
x2, y2 = 569, 347  

# Crop the region of interest from the image
cropped_region = image[y1:y2, x1:x2]

# Save the cropped region to a file
output_path = "cropped_region.jpg"  
cv2.imwrite(output_path, cropped_region)

# Display the cropped region
cv2.imshow("Cropped Region", cropped_region)
cv2.waitKey(0)
cv2.destroyAllWindows()