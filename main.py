import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_dir, dpi=300):
    """
    Convert a PDF into individual image files.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        output_dir (str): Directory to save extracted images.
        dpi (int): Resolution for image conversion (default: 300 DPI).
    
    Returns:
        List of image file paths.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)
    
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
    
    print(f"Saved {len(images)} images in {output_dir}")
    return image_paths

# Example usage:
pdf_path = "sample.pdf"  # Replace with actual PDF path
output_dir = "extracted_images"
pdf_to_images(pdf_path, output_dir)
import cv2
import os
import numpy as np

def extract_checks(image_path, output_dir):
    """Detects and extracts checks from an image."""
    
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    check_count = 0
    for contour in contours:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Filter based on expected check size (adjust as needed)
        if w > 100 and h > 50:  
            check = image[y:y+h, x:x+w]
            check_path = os.path.join(output_dir, f"check_{check_count + 1}.png")
            cv2.imwrite(check_path, check)
            check_count += 1

    print(f"Extracted {check_count} checks from {image_path}")

# Example usage
image_path = "extracted_images/page_1.png"  # Change as needed
output_dir = "extracted_checks"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

extract_checks(image_path, output_dir)
import zipfile

zip_path = r"C:\Users\pippa\Downloads\Release-24.07.0-0.zip\poppler-24.07.0\Library\bin.zip"
extract_to = "C:/Users/pippa/Desktop/poppler"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction complete!")

convert_from_path
images = convert_from_path(r"C\\Users\\pippa\\OneDrive\\Desktop\\dataset")
images[0].show()
import os

pdf_path = os.path.join(os.getcwd(), "sample.pdf")
from pdf2image import convert_from_path

pdf_path = r"C:\\Users\\pippa\\OneDrive\\Desktop\\dataset\\bank.pdf"  # Use raw string (r"") to avoid path issues
images = convert_from_path(pdf_path, poppler_path=r"C:\\Users\\pippa\Downloads\\Release-24.07.0-0\\poppler-24.07.0\\Library\bin\\pdfinfo.exe")

images[0].show()  # Display the first page
from pdf2image import convert_from_path

pdf_path = r"C:\\Users\\pippa\\OneDrive\\Desktop\\dataset\\bank.pdf"
poppler_path = r"C:\\Users\\pippa\Downloads\\Release-24.07.0-0\\poppler-24.07.0\\Library\bin\\pdfinfo.exe"

images = convert_from_path(pdf_path, poppler_path=poppler_path)
images[0].show()  # Display the first page
import os

pdf_path = r"C:\\Users\\pippa\\OneDrive\\Desktop\\dataset\\sample.pdf"

# Check if the file exists
if os.path.exists(pdf_path):
    print("File found:", pdf_path)
else:
    print("File NOT found:", pdf_path)
from pdf2image import convert_from_path
images = convert_from_path(pdf_path, poppler_path = r"C:\\path\\to\\poppler\\bin")
