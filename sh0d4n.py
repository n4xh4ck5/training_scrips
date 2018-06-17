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
	print "\n[*]Target: " + str(data['ip_str'])
	print "Country:" + str(data['country_name'])
	print "city:" + str(data['city'])
	print "Lattitude: " + str(data['latitude'])
	print "Longitudes: " + str(data['longitude'])
	print "Hostnames:" + str(data['hostnames'])
	print "Ports:"+ str(data['ports'])
	for x in data['data']:
		print "\nPort:" + str(x['port'])
		print "\nBanner:\n" + str(x['data'])
		print "Server: " + str(x["http"]["server"])

		
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
	API="YOUR_API_KEY"
	r = None
	array = None
	array = read_input(target) 
	for ip in array:
		url = "https://api.shodan.io/shodan/host/"+ip+"?key="+API
		print ip
		r = send_request(url)
		manage_response(r)

if __name__ == "__main__":
    main(sys.argv[1:])