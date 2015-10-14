#Assignment 1
# Zachary Seselja
# student # V00775627

#signing file which prepares application file to run

import sys
import time
import hashlib
import md5
import os
import module
import datetime
import rsa
import base64
import json
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES

from Crypto.Hash import SHA256
from Crypto import Random



def main():
	print ("Signing Document")
	exp = "2015-09-22"
	expiry = datetime.date(2015 , 9, 22)
	expirytext = "2015-09-22"
	

	Keyz = RSA.generate(1024 )
	priKey = Keyz.exportKey()
	pubKey = Keyz.publickey()
	
	message = 'Let the darkness flow through you'
	cipher = Keyz.publickey().encrypt(message , 32)
	cipherdate = Keyz.publickey().encrypt(exp , 32)
	

	ciphertext = cipher[0]
	cipherdatetext = cipherdate[0]

	
	cipherdate64 = base64.b64encode(cipherdatetext)
	cipher64 = base64.b64encode(ciphertext)
	# print cipher64
	signhash = SHA256.new(message).digest()
	# print signhash
	noencyrip = Keyz.decrypt(cipherdatetext)
	# print noencyrip
	signhash = unicode(signhash, errors='replace')
	
	
	dictonary = { 'time' : cipherdate64  , 'signature': cipher64 , 'encrypted-message' : signhash}
	json.dump(dictonary, open("licencefile.der",'w+'))
	keyfile = open('mypublickey.pem', 'wb')
	keyfile.write(Keyz.exportKey())

	

	
 
if __name__ == "__main__":
	main()	