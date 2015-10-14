#Assignment 1
# Zachary Seselja
# student # V00775627
import sys
import time

import md5
import os
import module
import datetime
from datetime import datetime
import rsa
import base64
import json
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES

from Crypto.Hash import SHA256
from Crypto import Random

def checklic(licence , exp ):
	licencelist = []
	licence = licence.read()
	licstring =''
	
	# print licence
	count  = 0
	b  = 0
	hit = 0
	Len = licence.__len__()

	for x in licence:
		licstring = licstring + x
	licencelist = licstring.split( ',' , 3)
	# print licencelist
	
	sig = licencelist[0].split(" ")
	time = licencelist[2].split(" ")
	
	timeexp = time[2]
	timeexp = timeexp[1:-1]
	
	sig64 = sig[1]
	sig64 = sig64[1:-1]
	
	ciphertexttime = base64.b64decode(timeexp )
	ciphertext = base64.b64decode(sig64 )
	
	# print cipher64
	keyfile = open('mypublickey.pem', 'rb')
	RSAKey = RSA.importKey(keyfile.read())

	# print RSAKey.exportKey()
	cleartime = RSAKey.decrypt(ciphertexttime)
	cleartext  = RSAKey.decrypt(ciphertext)
	print "Message:" + cleartext
	# print cleartime
	sequence =''
	# cleartime = (str)cleartime
	
	# ciphertextnew = RSAKey.publickey().encrypt(cleartext , 32)
	# ciphertextnew = ciphertextnew[0]


	#Now we have the message so we must check the hash
	newhash = SHA256.new(cleartext).digest()
	
	#This is comparing the hashes to check the signature
	hashholder = licencelist[1].split(" ")
	oldhash = hashholder[2]
	# print oldhash
	# print'\n'
	
	newhash = unicode(newhash, errors='replace')
	dictonary = { 'encrypted-message' : newhash}
	json.dump(dictonary, open("licencefile.der",'w+'))
	licence2 = open('licencefile.der', 'r')
	
	licencelist2 = []
	licence2 = licence2.read()
	licstring2 =''
	for x in licence2:
		licstring2 = licstring2 + x
	licencelist2 = licstring2.split( ',' , 3)
	newhash = licencelist2[0].split(" ")
	newhashcomp = newhash[1]
	newhashcomp = newhashcomp[:-1]
	# print newhashcomp

	if newhashcomp == oldhash:
		print "Licence is good"
		print "Checking expiry date"
		pass
	
	#checking the timestamp
	newexp = ''
	for char in cleartime:
		newexp = newexp + char
		pass
		# print newexp
	newexp = datetime.strptime(newexp, '%Y-%m-%d')
	# print newexp
	if exp < newexp:
		print 'Fail! Program Has Expired!'
		print 'Fail! Program Has Expired!'
		print 'Fail! Program Has Expired!'
		return 0

		pass
	else:
		print 'Time stamp is good!'
		print " . . . "
		print ". o o . "
		print ". \\_/ ."
		print " . . .  "
		print 
		return 1
	pass




def main():
	# print ("Looking for Licence")
	exp = "2015-09-24"
	exp = datetime.strptime(exp, '%Y-%m-%d')
	# print exp

	#opening and checking file. If not it should fail and quit.
	try:
		licence = open('licencefile.der', 'r')
		checklic(licence , exp)
	except IOError as e:
		print"\nNo Licence:\nTerminating program".format(e.errno, e.strerror)
		return 0 
		# smiley face
	




	
			


 
if __name__ == "__main__":
	main()	