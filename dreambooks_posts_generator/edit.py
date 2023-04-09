from PIL import Image
import os
import numpy

covers = os.listdir("./Covers_2.0")

cover_final_width = 409
cover_final_height = 681

cover_x_coor = 257
cover_y_coor = 147

def pasteImage(cover):
	# Opening the primary image (used in background)
	img1 = Image.open(r"./template.png")
	width1, height1 = img1.size

	# Opening the secondary image (overlay image)
	img2 = Image.open(f"./Covers_2.0/{cover}")

	img2_resized = img2.resize((cover_final_width, cover_final_height))
	width2, height2 = img2.size

	# Pasting img2 image on top of img1
	# starting at coordinates (0, 0)
	img1.paste(img2_resized, (cover_x_coor, cover_y_coor))
	# Saving the image
	img1.save(f"./Posts/{cover}", "PNG")
	img1.close()
	img2.close()

for cover in covers:
	pasteImage(cover)