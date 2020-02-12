from PIL import Image
import io
from urllib.request import urlopen
src = 'https://hy.captcha.qq.com/hycdn_1_1585332194439873792_0?aid=549000912&captype=&curenv=inner&protocol=https&clientype=2&disturblevel=&apptype=2&noheader=&color=&showtype=embed&fb=1&theme=&lang=2052&ua=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ny4wLjM4NjUuOTAgU2FmYXJpLzUzNy4zNg==&grayscale=1&subsid=3&sess=WP9IkTA6rCMaXcb42Skb-VlbykNSFTmlZe14d-a8P1xpfPcN5n0mciosFk-UW1jalTl9t5aHIDnfFue4sNBwxMoYQ5m5FtbZsk38zQf9qiNaU8nR09uNavMXHUxtiXakLemBl-Hcs5D7_CFSiVC1uPmuQAorYmj4666iHw6NI499LoHVOvK5oupDN8J6BbTf6v9W3JnD3RU*&fwidth=0&sid=6787722752690240442&forcestyle=undefined&wxLang=&tcScale=1&noBorder=noborder&uid=942138429&cap_cd=OlL7jc7dXTLSHK8irPQq4BMomfx26LYpPNFUD_Wvq02n5EYmEp_9lQ**&rnd=291310&TCapIframeLoadTime=97&prehandleLoadTime=27&createIframeStart=1580389858126&rand=74002632&websig=4a8060e6b84a13218f684bd088a67746259bbb2d9146c5b860ba8ad97ed50799e01e7debfeeb2f3d9eae7772b4269799c2c594e9a3073bf14cd818f4e21fbee6&vsig=c01zrGMRYGje3jzcRtre6DkYDjMbRuqzUzzbCKYj3FiALDTo_ZlULQQ6nSTgD6PkFsUMLPJiaBcjPrhmcpn0rRME13_iYNpxgPcuFLkuEQ5_oUpDZ5UUl1cMDRWCrcfLNf9w9L_ADFkN3BiU12p6e-iVYhXYWFIkl9yxVqJmHDbB83OKCOyvOsjGQ**&img_index=1'
data = urlopen(src).read();
bytes = io.BytesIO(data)
img = Image.open(bytes)
size = 280;
def checkPoint(times, checked, i, j, rightFlag):
	if (times == 0):
		return checked;
	else:
		times = times - 1;
	try:
		data = img.getpixel((i, j));
	except: 
		return 0;
	print(data)
	if (data[0] > 210 and data[1] > 210 and data[2] > 210):
		checked = checked + 1;
	if (rightFlag):
		return checkPoint(times, checked, i + 1, j, True);
	else:
		return checkPoint(times, checked, i, j + 1, False);
width = img.size[0];
height = img.size[1];
print(width)
x = 0;
'''
for i in range(0, width):
	for j in range(0, height):
		xCount = checkPoint(25, 0, i, j, True);
		yCount = checkPoint(25, 0, i, j, False);
		if (xCount > 22 and yCount > 22):
			x = j;
offset = x * size / width;
print('缺口偏移量: ' + str(offset))

'''

xCount = checkPoint(25, 0, 499, 116, True);
yCount = checkPoint(25, 0, 499, 116, False);
print(xCount)
print(yCount)