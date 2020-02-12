from PIL import Image, ImageColor, ImagePalette
from pathlib import Path
from PIL.ImageQt import rgb
from map_colours import MAP_COLOURS

INPUT_FOLDER = Path("input/")
INPUT_NAME = INPUT_FOLDER / "in.png"

IM_SIZE = 128


def load_im():
	if INPUT_NAME.exists():
		im = Image.open(INPUT_NAME)
	elif (INPUT_FOLDER / "in.jpg").exists():
		im = Image.open(INPUT_FOLDER / "in.jpg")
	else:
		im = ""
		print("Hey no png/jpg exists with the name \"in\"!\nDid you remember to put it in the input folder?")
		exit()
	temp = Image.new("RGBA", (128, 128), color=(255, 255, 255))

	if im.size[0] > IM_SIZE or im.size[1] > IM_SIZE:
		if im.size[0] > im.size[1]:
			im = im.resize((IM_SIZE, int(im.size[1] * IM_SIZE / im.size[0])), Image.BICUBIC)
		elif im.size[0] < im.size[1]:
			im = im.resize((int(im.size[0] * IM_SIZE / im.size[1]), IM_SIZE), Image.BICUBIC)
		else:
			im = im.resize((IM_SIZE, IM_SIZE), Image.BILINEAR)
	temp.paste(im, mask=im)
	im = temp
	im.save("im.png")


def distance(colour1, colour2):
	(r1, g1, b1, a1) = colour1
	(r2, g2, b2, a2) = colour2
	return abs((r1 - r2) * (r1 - r2) + (g1 - g2) * (g1 - g2) + (b1 - b2) * (b1 - b2))


def get_closest_to_palette(colour):
	x = 7000000  # random high number
	col = (0, 0, 0, 0)
	for clr in MAP_COLOURS:
		temp = distance(clr.get("rgba_mid"), colour)
		if temp <= x:
			x = temp
			col = clr.get("rgba_mid")
	return col


def convert_im():
	IM = Path("im.png")
	if not IM.exists():
		print("No file was found with the name \"im.png\"!")
		exit()
	im = Image.open(IM)
	# px = im.load()

	# pal = []
	# for clr in MAP_COLOURS:
	# 	pal.append(clr.get("rgba")[0])
	# #for clr in MAP_COLOURS:
	# 	pal.append(clr.get("rgba")[1])
	# #for clr in MAP_COLOURS:
	# 	pal.append(clr.get("rgba")[2])
	# print(pal)
	# pal = [int(i*220/255) for i in pal]
	# print(pal)
	# for clr in MAP_COLOURS:
	# 	pal.append(clr.get("rgba")[3])

	# im3 = im.copy()
	#
	# im3 = im3.quantize(colors=50, method=2, kmeans=0)
	# #im3.putpalette(pal)
	# im3.show()
	#
	# im5 = Image.new("P", (128, 128), 0)
	# im5.putpalette(pal)
	# im5.paste(im3)
	# im5.show()

	# new_image = Image.new('P', im3.size)
	# new_image.putpalette(pal * 50)
	# new_image.paste(im3, (0, 0) + im3.size)
	# new_image.show()

	# 220/255 is the scale factor for a flat image
	# for x in range(im.size[0]):
	# 	for y in range(im.size[1]):
	# 		r, g, b, a = get_closest_to_palette(im.getpixel((x, y)))
	# 		closest_clr = r, g, b, a
	# 		px[x, y] = closest_clr

	for x in range(im.size[0]):
		for y in range(im.size[1]):
			r, g, b, a = get_closest_to_palette(im.getpixel((x, y)))
			closest_clr = r, g, b, a
			im.putpixel((x, y), closest_clr)

	im.show()
	im.save("im2.png")


def math_im():
	IM2 = Path("im2.png")
	if not IM2.exists():
		print("No file was found with the name \"im.png\"!")
		exit()
	im = Image.open(IM2)

	block_count = [0] * 50
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			# r, g, b, a = im.getpixel((x, y))
			#print(im.getpixel((x, y)))
			pass


load_im()
convert_im()

# TODO: add math functions that will calculate how many resources are needed to build it.
# first, loop through the image, adding one for each pixel seen with a certain id into an array 51 long
# then just count, then get the cool totls
# gotta divide by 64, mod 64 to get num of stacks
# mining/aquiring stats?
# TODO: add ability to remove certain blocks/colours
# TODO: GUI ?????????????


# def get_all_mapclr():
# 	for clr in MAP_COLOURS:
# 		r, g, b, a = clr.get("rgba")
# 			print(clr.get("name"), ":\n\"rgba\": (", r, ',', g, ',', b, ',', 255, "), \n\"rgba_mid\": (",
# 	  		int(r * 220 / 255), ',', int(g * 220 / 255), ',', int(b * 220 / 255), ',', 255, "), \n\"rgba_dark\": (",
# 	 		 int(r * 180 / 255), ',', int(g * 180 / 255), ',', int(b * 180 / 255), ',', 255, '),\n')