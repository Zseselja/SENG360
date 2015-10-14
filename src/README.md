# SENG360
Software Engineering security course

Project one is a simple signature checking program which decryptics a hashed message via public key to check if the signature is valid.
The code was written in python 2.10.0.

Within this zip file is 5 files:
1.Application.py 
	- The file which checks the signature and expiry date.
2.signer.py
	- This file signs the licencefile.der and provides the key through mypublickey.pem
3.licencefile.der
	- Stores the encrtyped information for the licence and expiry date
4.mypublickey.pem
	- Store the public key for the Application file
5. README

*Note I developed this code running python 2.10 on windows 7
*Also I downloaded the libraries Pycryto and RSA

Some thoughts about how someone would break this:
1. If they got hold of the key folder
2. If they caused the decrypttion process to fail it could give them clues to what scheme I used.
