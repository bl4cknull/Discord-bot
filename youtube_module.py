from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import linkshortner

options = Options()
options.add_argument('--log-level=3')
options.add_argument('--disable-gpu')


def get_download_link(link):
	driver = webdriver.Chrome('C:\Program Files (x86)\Chromedriver.exe', options=options)
	driver.get('https://en.savefrom.net/1-youtube-video-downloader-5/')
	send_link = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/input')
	send_link.send_keys(link)
	submit = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/form/div[2]')
	submit.click()
	time.sleep(2)
	button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a')
	result_link = button.get_attribute("href")
	final_link = linkshortner.link_shortner(result_link)
	driver.close()
	return final_link


