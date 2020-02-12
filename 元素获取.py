print('欢迎使用:)');
#	引入sys,添加selenium路径
import sys
#	路径配置到__init__.py上一层
sys.path.append('D:\selenium//selenium-3.141.0');
#	引入配置好的selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#	指定chrome驱动的路径并启动[注意驱动和chrome版本号的对应]
chrome = webdriver.Chrome('D://selenium//chromedriver.exe');
chrome.implicitly_wait(10);
chrome.get('C://Users//Administrator//Desktop//aaa.html');
'''
#	打开说说画面
speak = chrome.find_element_by_xpath('//a[@accesskey="6"]');
speak.click();
'''

'''
#	获得当前页说说内容
content = chrome.find_elements_by_xpath('//div[@class="bd"]/pre[@class="content"]');
print(len(content))
for index in range(len(content)):
	print(content[index].text)
'''


#	获得当前页说说内容
content = chrome.find_elements_by_xpath('//div[@class="bd"]/pre[@class="content"]');
times = chrome.find_elements_by_xpath("//a[contains(@class,'c_tx c_tx3')]");

import os
import shutil
import time
if (os.path.exists('G://speak_log')):
	shutil.rmtree('G://speak_log');
os.makedirs('G://speak_log');
	
def getPageInfo():
	for index in range(len(content)):
		print('G://speak_log//' + times[index].get_attribute('title').replace(':', '.') + '.txt')
		file = open('G://speak_log//' + times[index].get_attribute('title').replace(':', '.') + '.txt', 'w');
		file.write(content[index].text);
		file.close();
	try:
		next = chrome.find_element_by_xpath('//p[@class="mod_pagenav_main"]/a[@title="下一页"]');
		next.click();
		time.sleep(5);
		getPageInfo();
	except Exception as e:
		print('遍历结束...');
		print(e)
getPageInfo()