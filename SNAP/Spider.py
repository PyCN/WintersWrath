#coding = utf-8
import time
import comm
from urlparse import *
from termcolor import cprint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def claw_url(original_url, skip_url):
	if(skip_url != ''):
		try:
			driver.get(skip_url)
		except:
			cprint("Waiting time too long,so we skip the loading program~~",'red')
		cprint( "Current_url:%s" % driver.current_url, 'green')

		url_info = urlparse( driver.current_url )

		comm.write_url_redis( original_url, driver.current_url )

		driver.get_screenshot_as_file("/tmp/SitePic/"+url_info.netloc+".png")

def get_input(filename):
	input = open(filename)

	for line in input:
		claw_url( line[:-1], comm.get_302_url(line[:-1]) )
		#claw_url( line[:-1] )

if __name__ == "__main__":
	comm.set_logging()
	comm.connect_to_redis(0)

	driver = webdriver.PhantomJS('/home/elfsong/phantomjs-2.1.1/bin/phantomjs')
	driver.implicitly_wait(8)

	get_input("input.txt")
	
	driver.quit()
