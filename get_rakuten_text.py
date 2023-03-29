# -*- coding: utf-8 -*-

# https://www.seleniumqref.com/api/webdriver_gyaku.html
# import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

CHROMEDRIVER = "/usr/bin/chromedriver"

def check_exists(driver,temp_by,temp_by_str):
	try:
		driver.find_element(temp_by,temp_by_str)
	except NoSuchElementException:
		return False
	return True

def main():

	f = open("id.txt", "r")

	id_str = f.readline()
	id_str = id_str.rstrip('\n')

	pass_str = f.readline()
	pass_str = pass_str.rstrip('\n')

	f.close()

	url = ""

	#　ヘッドレスモードでブラウザを起動
	options = Options()
	#    options.add_argument('--headless')

	chrome_service = fs.Service(executable_path=CHROMEDRIVER)
	driver = webdriver.Chrome(service=chrome_service)

	driver.get(url)
	# 1秒でタイムアウト判定
	# wait = WebDriverWait(driver, 1)
	wait = WebDriverWait(driver, 5)

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#u"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.send_keys(id_str)

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#p"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.send_keys(pass_str)

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#loginButton"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.click()

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#js-rd-billInfo > div.rd-column-cell.rd-billInfo-month > div.rd-billInfo-table > div.rd-billInfo-table_month.rd-flex > div.rd-billInfo-table_date > div > div.rd-font-robot"
	wait.until(expected_conditions.visibility_of_element_located((temp_by, temp_by_str)))
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print (temp_elm.text, end="\t")

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#js-rd-billInfo > div.rd-column-cell.rd-billInfo-month > div.rd-billInfo-table > div.rd-billInfo-table_billing.rd-flex > div.rd-billInfo-table_amount.rd-flex > div.rd-billInfo-amount.rf-font-bold > span"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print (temp_elm.text, end="\t")

	temp_by = By.CSS_SELECTOR
	temp_by_str = "#js-rd-billInfo-amount_show > span"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print (temp_elm.text)

	input_result = input("wait")

	# ブラウザ停止
	driver.quit()

if __name__ == '__main__':
	main()
