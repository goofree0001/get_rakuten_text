#!/usr/bin/ruby
# -*- coding: utf-8 -*-
#$KCODE = 'UTF8'

require 'selenium-webdriver'


def main()

	f = open("id.txt", "r")

	id_str = f.readline()
	id_str = id_str.chomp

	pass_str = f.readline()
	pass_str = pass_str.chomp

	f.close()

	url = ""
	driver = Selenium::WebDriver.for :chrome

	# 10秒でタイムアウト判定
	driver.manage.timeouts.implicit_wait = 10

	driver.navigate.to url

	temp_by = :css
	temp_by_str = "#u"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.send_keys(id_str)

	temp_by = :css
	temp_by_str = "#p"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.send_keys(pass_str)

	temp_by = :css
	temp_by_str = "#loginButton"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	temp_elm.click()

	temp_by = :css
	temp_by_str = "#js-rd-billInfo > div.rd-column-cell.rd-billInfo-month > div.rd-billInfo-table > div.rd-billInfo-table_month.rd-flex > div.rd-billInfo-table_date > div > div.rd-font-robot"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print temp_elm.text
	print "\t"

	temp_by = :css
	temp_by_str = "#js-rd-billInfo > div.rd-column-cell.rd-billInfo-month > div.rd-billInfo-table > div.rd-billInfo-table_billing.rd-flex > div.rd-billInfo-table_amount.rd-flex > div.rd-billInfo-amount.rf-font-bold > span"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print temp_elm.text
	print "\t"

	temp_by = :css
	temp_by_str = "#js-rd-billInfo-amount_show > span"
	temp_elm = driver.find_element(temp_by, temp_by_str)
	print temp_elm.text
	puts

	puts "wait"
	input = gets

	driver.quit

end

if $0 == __FILE__
	main()
end
