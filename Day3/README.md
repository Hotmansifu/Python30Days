first, make sure you have the PIL library installed in your machine by running pip install pillow.

Download or clone the repository to your local machine, the script is located in the main.py file.

Open the main.py file, you can use any text editor.

In the watermarkforpictures.py file, you will find the following line image = Image.open("image.png"), replace the "image.png" with the path of the image you want to add the watermark to.

In the watermarkforpictures.py file, you will find the following line watermark = Image.open("watermark.png"), replace the "watermark.png" with the path of the watermark you want to add to the image.

You can adjust the size of the watermark by changing the value of the watermark.resize() method, the script resizes the watermark to be 1/4 the size of the original image, you can adjust the value as per your needs.

You can adjust the position of the watermark by changing the value of the position variable, the script sets the position to be in the top-left corner, you can adjust the values of x and y as per your needs.

You can adjust the transparency of the watermark by changing the value of the watermark_pixel[i, j] method, the script sets the transparency to be 50%, you can adjust the value as per your needs.

Once you've made the necessary changes, save the main.py file.

Open a command prompt or terminal window and navigate to the directory where the script is located.

Run the script by typing python main.py and press enter.

The script will add the watermark to the image and save the output as "output.png" in the same directory where the script is located.

You can change the output image name by changing the value of the output.save() method.


................Keep in mind  in "watermarked.paste(watermark, (int(image_width*w),int(image.height*h)), watermark)" w and h values should be chosen individually depending on the size of a template 
