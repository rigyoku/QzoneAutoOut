print('欢迎使用:)');
#	引入sys,添加selenium路径
import sys
#	路径配置到__init__.py上一层
sys.path.append('D:\selenium\selenium-3.141.0');
#	引入配置好的selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#	指定chrome驱动的路径并启动[注意驱动和chrome版本号的对应]
chrome = webdriver.Chrome('D://selenium//chromedriver.exe');
#	最大化
chrome.maximize_window();
#	指定打开的url
chrome.get('https://user.qzone.qq.com');
#	设置隐性等待时间10s[注意只需要设置一次即可]
chrome.implicitly_wait(10);
#	切换到指定的iframe
chrome.switch_to.frame(chrome.find_element_by_xpath('//iframe[@id="login_frame"]'));
#	显性等待el[账户密码登录]加载
userAndPassLogin = WebDriverWait(chrome, 8).until(lambda chrome: chrome.find_element_by_xpath('//a[@id="switcher_plogin"]'));
userAndPassLogin.click();

print('请输入用户名和密码...');

username = chrome.find_element_by_xpath('//input[@id="u"]');
username.send_keys(input('请输入用户名\n'));

password = chrome.find_element_by_xpath('//input[@id="p"]');
password.send_keys(input('请输入密码\n''));

loginBtn = chrome.find_element_by_xpath('//input[@id="login_button"]');
loginBtn.click();
print('正在处理滑块验证码...');

'''
如果使用PIL完成二值化可以执行命令pip install pillow安装PIL

user下面创建pip目录,创建pip.ini文件,并输入内容以下完成国内镜像的

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
'''

'''
如果使用cv2转换图片可以执行命令安装CV2
pip install opencv-python
'''


import io
from urllib.request import urlopen
import cv2
import numpy

#	切换到指定的iframe
chrome.switch_to.frame(chrome.find_element_by_xpath('//iframe[@id="tcaptcha_iframe"]'));

offset = 0;
while (offset < 140):
	if (offset == 0):
		pass;
	else:
		reload = chrome.find_element_by_xpath('//div[@id="e_reload"]');
		reload.click();
	#	找到bg
	WebDriverWait(chrome, 8).until(lambda chrome: chrome.find_element_by_xpath('//img[@id="slideBg"]').get_attribute('src') != None);
	slideBg = chrome.find_element_by_xpath('//img[@id="slideBg"]');
	bgSrc = slideBg.get_attribute('src');
	size = slideBg.get_attribute('width');
	#	找到block
	WebDriverWait(chrome, 8).until(lambda chrome: chrome.find_element_by_xpath('//img[@id="slideBlock"]').get_attribute('src') != None);
	slideBlock = chrome.find_element_by_xpath('//img[@id="slideBlock"]');
	blockSrc = slideBlock.get_attribute('src');

	#	计算缺口位置
	bgData = urlopen(bgSrc).read();
	bg = cv2.imdecode(numpy.array(bytearray(bgData), dtype=numpy.uint8), -1);
	#	二值化图片
	bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY);

	blockData = urlopen(blockSrc).read();
	block = cv2.imdecode(numpy.array(bytearray(blockData), dtype=numpy.uint8), -1);
	block = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY);
	#	截掉边缘
	block = block[41:95, 41:95]
	#	图片比较
	diff = cv2.matchTemplate(bg, block, cv2.TM_CCOEFF_NORMED);
	#	取最大值时x坐标
	offset = cv2.minMaxLoc(diff)[3][0];
	#	根据像素和画面大小进行缩放
	bgWidth = bg.shape[1];
	offset = int(offset - 41) * int(size) / int(bgWidth)

print('偏移量为 ：' + str(offset));
			
#	找到滑块
#	TODO: 写成方法，失败时重新调用
slideBlock = chrome.find_element_by_xpath('//img[@id="slideBlock"]');
chrome.execute_script("arguments[0].style.left='" + str(offset) + "px';", slideBlock);
slideBlock.click();

#	打开说说画面
speak = chrome.find_element_by_xpath('//a[@accesskey="6"]');
speak.click();
chrome.switch_to.frame(chrome.find_element_by_xpath('//iframe[@class="app_canvas_frame"]'));

import os
import shutil
import time

if (os.path.exists('G://speak_log')):
	shutil.rmtree('G://speak_log');
os.makedirs('G://speak_log');
page = 0;

def getPageInfo(page):
	
	#	获得当前页说说内容
	content = chrome.find_elements_by_xpath('//div[@class="bd"]/pre[@class="content"]');
	#	选择包含该class的元素
	times = chrome.find_elements_by_xpath("//a[contains(@class,'c_tx c_tx3')]");
	for index in range(len(content)):
		print('G://speak_log//' + times[index].get_attribute('title').replace(':', '.') + '.txt')
		file = open('G://speak_log//' + times[index].get_attribute('title').replace(':', '.') + '.txt', 'w', encoding='utf-8');
		file.write(content[index].text);
		file.close();
	try:
		next = chrome.find_element_by_xpath('//a[@id="pager_next_' + str(page) + '"]');
		next.click();
		time.sleep(5);
		page = page + 1;
		getPageInfo(page);
	except Exception as e:
		print('遍历结束...');
		print(e)
getPageInfo(page);