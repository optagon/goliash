from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time, random
from selenium.common.exceptions import *
from motorbikes import words


class InstagramBot:

	def __init__(self, username, password):
		
		self.username = input("Username: ")
		self.password = input("Password:: ")
		self.driver = webdriver.Chrome('./chromedriver.exe')
		self.search()

	def search(self):
		#login user
		self.driver.get('https://www.instagram.com/accounts/login/')
		time.sleep(1) #sleep for latency in loading the page
		#login user and press login button
		self.driver.find_element_by_name("username").send_keys(self.username)
		self.driver.find_element_by_name("password").send_keys(self.password)
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
		time.sleep(3)
		#set counter to monitor how many iterations will be executed
		counter = 0

		#iterate 300 times | it takes about 300 likes to alter your instagram persona
		for i in range(300):
			row = random.randrange(1,2)
			col = random.randrange(1,3)
			#query = random.choice(words)
			#choose from the array of topics
			#index = random.randrange(len(query))
			self.search = random.choice(words)
			print(self.search)
			#open tags with the given search tag
			self.driver.get('https://www.instagram.com/explore/tags/' + self.search)
			time.sleep(random.randrange(0,6))
			#follow the tag
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/button').click()
			time.sleep(random.randrange(0,6))
			print("following a tag " + self.search)
			#unfollow the tag righ away
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/button').click()
			time.sleep(random.randrange(0,6))
			print("unfollowing a tag " + self.search)
			#select a post 
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+ str(row) +']/div['+ str(col)+']/a/div').click()
			time.sleep(random.randrange(0,6))
			#like the post
			try:
				self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
				time.sleep(random.randrange(0,6))
				print("post [" + str(row) + "] [" + str(col) + "] liked")
				#unlike the post
				self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
				print("post [" + str(row) + "] [" + str(col) + "] unliked")
			#set a counter to monitor the iterations
			except NoSuchElementException:
				pass
			counter = counter +1 
			print("iteration no: " + str(counter) +" finished")

if __name__ == '__main__':
	ig_bot = InstagramBot('temp_username', 'temp_password')
	print(ig_bot.username)
