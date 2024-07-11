from PIL import Image
import os

def load_images(image_dir, rows, cols):
    """
    Load images from a directory and return them in a 2D list (row-wise).

    Parameters:
    image_dir (str): Directory containing the images.
    rows (int): Number of rows in the final stitched image.
    cols (int): Number of columns in the final stitched image.

    Returns:
    list of list of Image: 2D list containing the loaded images.
    """
    images = []
    for i in range(rows):
        row_images = []
        for j in range(cols):
            image_path = os.path.join(image_dir, f'part_{i}_{j}.png')
            with Image.open(image_path) as img:
                row_images.append(img.copy())
        images.append(row_images)
    return images

def stitch_images(images):
    """
    Stitch a 2D list of images into a single image.

    Parameters:
    images (list of list of Image): 2D list containing the images to be stitched.

    Returns:
    Image: The final stitched image.
    """
    # Get dimensions of each part (assuming all parts are the same size)
    part_height = images[0][0].height
    part_width = images[0][0].width

    # Calculate dimensions of the final stitched image
    total_height = part_height * len(images)
    total_width = part_width * len(images[0])

    # Create a new blank image with the total dimensions
    stitched_image = Image.new('RGB', (total_width, total_height))

    # Paste each part into the final image
    for i, row in enumerate(images):
        for j, img in enumerate(row):
            stitched_image.paste(img, (j * part_width, i * part_height))

    return stitched_image

# Main function to load images, stitch them, and save the final image
def main(image_dir, rows, cols, output_path):
    images = load_images(image_dir, rows, cols)
    stitched_image = stitch_images(images)
    stitched_image.save(output_path)
    print("Image has been stitched and saved successfully.")

# Parameters
image_dir = ''  # Directory containing the images
rows = 110  # Number of rows in the final stitched image
cols = 78  # Number of columns in the final stitched image
output_path = 'stitched_image.jpg'  # Output path for the stitched image

# Run the main function
main(image_dir, rows, cols, output_path)
