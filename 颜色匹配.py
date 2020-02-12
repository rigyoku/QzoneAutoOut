from PIL import Image
img1 = Image.open('G:/QzoneAutoOut/1.jpg')
img2 = Image.open('G:/QzoneAutoOut/2.png')
'''
#	获取指定像素点RGB
#	print(img1.getpixel((476, 56)))
#	裁剪
img2Temp = img2.crop((25, 25, 113, 113))
#	粘贴图片
#	566 / 478 / 143 / 55
#img2 = img2.convert('RGB')
img1.paste(img2Temp, (478, 55))
img1.save('G://QzoneAutoOut//3.jpg')
'''
'''
img1Temp = img1.crop((478, 55, 566, 143))
img1Temp.save('G://QzoneAutoOut//3.jpg')
'''
'''
img3 = Image.open('G:/QzoneAutoOut/3.jpg')
img3 = img3.convert('L')
img3.save('G://QzoneAutoOut//4.jpg')
'''
'''
img2Temp = img2.crop((25, 25, 113, 113))
img2Temp = img2Temp.convert('L')
img2Temp.save('G://QzoneAutoOut//5.png')
'''
'''
img3 = Image.open('G:/QzoneAutoOut/3.jpg')
img3 = img3.convert('RGBA')
print(img3.getpixel((45, 48)))
'''
'''
width = img1.size[0]
height = img1.size[1]
for i in range(0, width):
	for j in range(0, height):
		data = img1.getpixel((i, j))
		img1.putpixel((i, j), (data[0] + 70, data[1] + 110, data[2] + 70))
img1.save('G://QzoneAutoOut//6.jpg')
'''


def checkPoint(times, checked, i, j, rightFlag):
	if (times == 0):
		return checked;
	else:
		times = times - 1;
	try:
		data = img1.getpixel((i, j))
	except: 
		return 0;
	if (data[0] > 222 and data[1] > 222 and data[2] > 222):
		checked = checked + 1;
	if (rightFlag):
		return checkPoint(times, checked, i + 1, j, True);
	else:
		return checkPoint(times, checked, i, j + 1, False);

width = img1.size[0]
height = img1.size[1]
for i in range(0, width):
	for j in range(0, height):
		xCount = checkPoint(25, 0, i, j, True);
		yCount = checkPoint(25, 0, i, j, False);
		if (xCount > 22 and yCount > 22):
			print(str(i) + ' -- ' + str(j));


'''
xCount = checkPoint(25, 0, 476, 53, True);
yCount = checkPoint(25, 0, 476, 53, False);
print(str(xCount) + ' -- ' + str(yCount));
'''