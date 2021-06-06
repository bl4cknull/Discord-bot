from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()
options.add_argument('--log-level=3')
options.add_argument('--disable-gpu')
def save_file(text):
	file = open('data.json', 'w')
	file.write(text)

def get_data(insta_id):
	driver = webdriver.Chrome('C:\Program Files (x86)\Chromedriver.exe', options=options)
	driver.get("https://www.instagram.com/{}/?__a=1".format(insta_id))
	text = driver.find_element_by_xpath('/html/body/pre').text
	save_file(text)
	driver.close()

def get_follower(insta_id):
	get_data(insta_id)
	f = open('data.json',)
	data = json.load(f)
	number = data["graphql"]['user']['edge_followed_by']['count']
	return number

