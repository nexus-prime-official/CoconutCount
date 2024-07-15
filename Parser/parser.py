from PIL import Image
import numpy as np

# Increase the max image pixels limit
Image.MAX_IMAGE_PIXELS = None

try:
    # Open the TIFF file
    tiff_image = Image.open('Tif file.tif')
    
    # Convert the image to a NumPy array
    image_array = np.array(tiff_image)
    
    # Define the size of the smaller parts
    part_height = 224  # Height of each part
    part_width = 224   # Width of each part

    # Get the dimensions of the image
    height, width = image_array.shape[:2]

    # Calculate the number of parts
    num_parts_height = height // part_height
    num_parts_width = width // part_width

    # Loop through the image array and save the parts
    for i in range(num_parts_height):
        for j in range(num_parts_width):
            # Calculate the coordinates of the current part
            start_row = i * part_height
            end_row = start_row + part_height
            start_col = j * part_width
            end_col = start_col + part_width
            
            # Extract the part from the image array
            part = image_array[start_row:end_row, start_col:end_col]
            
            # Convert the part back to an image
            part_image = Image.fromarray(part)
            
            # Save the part as a new image file
            part_image.save(f'part_{i}_{j}.png')

    print("Image has been split into smaller parts successfully.")
except Image.DecompressionBombError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
