#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json



def read_input(path):
	d = []
	try:

		with open (path) as f:
			lines = f.readlines()
			for line in lines:
				d.append(line.rstrip('\n'))
			f.close()

	except Exception as e:
		print e
	
	finally:
		return d

def manage_response (data):

	print "Status: " + str(data["status"])
	print "Status: " + str(data["country"])
	print "Status: " + str(data["city"])
	print "Status: " + str(data["whoisdesc"])
	print "Status: " + str(data["asname"])
	print "Status: " + str(data["bgproute"])
	

def send_request (url):

	response = None

	try:

		response = requests.get(url,timeout=5,allow_redirects =True)

	except Exception as e:
		print e

	finally:
		return response.json()


def main(argv):

	target = str(sys.argv[1])
	r = None
	array = None
	url = " https://freeapi.robtex.com/ipquery/"

	array = read_input(target) 
	for ip in array:
		print ip
		r = send_request(url+ip)
		manage_response(r)

if __name__ == "__main__":
    main(sys.argv[1:])