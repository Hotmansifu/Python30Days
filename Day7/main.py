from PIL import Image
import os

def resize_image(input_path, output_path, width=None, height=None, quality=100, reduce_by=None):
    with Image.open(input_path) as img:
        # Determine new size
        if width and height:
            new_size = (width, height)
        elif width:
            wpercent = (width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            new_size = (width, hsize)
        elif height:
            hpercent = (height / float(img.size[1]))
            wsize = int((float(img.size[0]) * float(hpercent)))
            new_size = (wsize, height)
        else:
            new_size = img.size

        # Reduce size by percentage if requested
        if reduce_by:
            new_size = tuple(int(dim * (1 - (reduce_by / 100))) for dim in new_size)

        # Resize the image
        img = img.resize(new_size, resample=Image.LANCZOS)

        # Save the image
        img.save(output_path, optimize=True, quality=quality)

if __name__ == '__main__':
    # Prompt user for input
    input_path = input("Enter path to input image: ")
    if not os.path.exists(input_path):
        print("Error: Input file does not exist")
        exit()

    output_path = input("Enter path to output image: ")

    width_str = input("Enter new width (leave blank to maintain aspect ratio): ")
    if width_str:
        width = int(width_str)
    else:
        width = None

    height_str = input("Enter new height (leave blank to maintain aspect ratio): ")
    if height_str:
        height = int(height_str)
    else:
        height = None

    quality_str = input("Enter quality level (0-100, default is 100): ")
    if quality_str:
        quality = int(quality_str)
    else:
        quality = 100

    reduce_str = input("Would you like to reduce the image size by a percentage? (y/n): ")
    if reduce_str.lower() == 'y':
        reduce_by_str = input("Enter percentage to reduce image by: ")
        reduce_by = int(reduce_by_str)
    else:
        reduce_by = None

    # Resize the image
    resize_image(input_path, output_path, width=width, height=height, quality=quality, reduce_by=reduce_by)

    print("Image resized and saved to", output_path)
