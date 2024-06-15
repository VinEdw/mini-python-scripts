from PIL import Image

# Open the two images
im_1 = Image.open("image_1.png")
im_2 = Image.open("image_2.png")
# Note the dimensions
width, height = im_1.size
# Create an output image to store where the two images differ
im_out_1 = Image.new("RGB", im_1.size, 0xffffff)
im_out_2 = Image.new("RGB", im_1.size, 0xffffff)

# Loop through each pixel
for x in range(width):
    for y in range(height):
        # Get the colors of the pixel
        color_1 = im_1.getpixel((x, y))
        color_2 = im_2.getpixel((x, y))
        # Compare the pixel colors
        # If they match, copy the color from image 2 to output 2
        # Otherwise, copy the color from image 2 to output 1
        if color_1 == color_2:
            im_out_2.putpixel((x, y), color_2)
        else:
            im_out_1.putpixel((x, y), color_2)

# Save the output images
im_out_1.save("blank_background_diff_image_2.png")
im_out_2.save("image_2_background_diff_blank.png")
