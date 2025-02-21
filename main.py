import os
import pdf2image
from pathlib import Path

def convert_pdf_to_images(pdf_path, output_folder, dpi=300, poppler_path=None):
    """
    Convert a multi-page PDF into individual image files.

    :param pdf_path: Path to the input PDF file.
    :param output_folder: Directory where images will be saved.
    :param dpi: Dots per inch for image quality (default is 300 DPI).
    :param poppler_path: Path to Poppler bin folder (needed for Windows).
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Error: PDF file not found at {pdf_path}")

    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF to images
    images = pdf2image.convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

    # Save each page as an image
    image_paths = []
    for i, image in enumerate(images):
        image_filename = f"page_{i + 1}.png"
        image_path = os.path.join(output_folder, image_filename)
        image.save(image_path, "PNG")
        image_paths.append(image_path)

    if not image_paths:
        raise RuntimeError("Error: No images were generated from the PDF!")

    print("Generated image paths:", image_paths)  # Debugging output
    return image_paths

if __name__ == "__main__":
    poppler_path = "C:\\Users\\pippa\\Downloads\\Release-24.07.0-0.zip\\poppler-24.07.0\\Library\\bin" # Update with the correct Poppler path
    pdf_path = "C:\\Users\\pippa\\OneDrive\\Desktop\\TASK1\\bank.pdf"  # Corrected PDF file path
    output_dir = "C:\\Users\\OneDrive\\Desktop\\TASK1\\output_images"  # Corrected output directory

    try:
        image_files = convert_pdf_to_images(pdf_path, output_dir, poppler_path=poppler_path)
        print("Images saved:", image_files)
    except Exception as e:
        print("Error:", str(e))
