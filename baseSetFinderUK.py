#!/usr/bin/python
#Pokemon bas
#standard imports
import sys
import os
import random
import re
from string import printable

#colours just in case for terminal
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
PURPLE = "\033[0;35m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

#headers stop http 403 responses :)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#import some good stuff to use later
try:
	from bs4 import BeautifulSoup
	import requests
	print "imports complete"
except ImportError:
	print "BeautifulSoup is not installed. Try 'sudo pip install beautifulsoup4'"

def scrape():
	print "\n***Looking around for available cards..."

	url="https://www.bigorbitcards.co.uk/pokemon/base-set/"
	req = requests.get(url, headers = headers)
	data = req.text
	soup = BeautifulSoup(data,'html.parser')

	format(soup)

def format(soup):
	print "Formating Data..."
	results = []
	cardTitles = []
	cardTitles2 = []
	cardPrices = []
	cardPrices2 = []
	cardStock = []


	#All results in one array - messy
	for div in soup.find_all('div', attrs={'class':'ty-product-list__content'}):
		if len(div.text)>0:
			results.append(div.text)

	#------------TITLES-------------------------------------------------------
	#Put all titles in an array, ready for printing later on
	for a in soup.find_all('a', attrs={'class':'product-title'}):
		if len(a.text)>0:
			cardTitles.append(a.text)
	#clean up the title array
	for i in range(len(cardTitles)):
		currentString = cardTitles[i]
		currentString = currentString.encode('ascii', 'ignore')
		cardTitles2.append(currentString)
		print currentString
	print len(cardTitles2)


	#------------PRICES-------------------------------------------------------
	for div in soup.find_all('div', attrs={'class': 'ty-product-list__price'}):
		if len(div.text)>0:
			cardPrices.append(div.text)
	#clean up the prices array
	for i in range(len(cardPrices)):
		currentString = cardPrices[i]
		currentString = currentString.encode('ascii', 'ignore')
		cardPrices2.append(currentString)
		print currentString
	print len(cardPrices2)


	#cardPrices = "\n".join(cardPrices)
	

	#----------STOCK-----------------------------------------------------------
	for i in range(len(results)):
		currentString = results[i]
		currentString = currentString.encode('ascii', 'ignore')
		#cardTitle = soup.find('a', attrs={'class':'product-title'})
		#cardTitle = cardTitle.text
		for i in range(len(currentString)):
			
			currentString = currentString.rstrip()
		

			if currentString[i:i+12]=="Out of stock":
				#results.remove(results[i])
				sys.stdout.write(RED)
				
				cardStock.append('out of stock')
				print ' @@@@@@@@ OUT OF STOCK :('
				#sys.stdout.write(GREEN)
				#print cardTitle
				sys.stdout.write(RED)
				currentString = currentString.rstrip()
				#print currentString

			if currentString[i:i+11]=="Add to cart":
				sys.stdout.write(GREEN)
				cardStock.append('out of stock')
				print 'IN STOCK!!! GO BUY HERE:'
				
				#currentString = re.sub("[^{}]+".format(printable), "", currentString)
				#print currentString
			#Out of stock



	print len(cardStock)

	#results = "\n".join(results)
	#print results
	#print len(results)
	
	#row result
	#print(soup)


scrape()

exit()




