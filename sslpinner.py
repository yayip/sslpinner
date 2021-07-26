#! /usr/bin/python3

from optparse import OptionParser
import os, sys

usage = sys.argv[0] + " Options "
parser = OptionParser(usage)
parser.add_option("-d","--der", dest="der", default=False, metavar="der", help="DER Cerfiticate")
parser.add_option("-p","--pem", dest="pem", default=False, metavar="pem", help="PEM Cerfiticate")
(options, args) = parser.parse_args()

def pinner(cert):
	os.system("openssl x509 -in " + cert + " -pubkey -noout | openssl rsa -pubin -outform der | openssl dgst -sha256 -binary | openssl enc -base64")

try:
	if __name__ == '__main__':
		if options.der != True and options.pem != True:
			if options.der:
				os.system("mkdir tmp")
				os.system("openssl x509 -inform der -in " + options.der + " -out tmp/cert.pem -pubkey")
				pinner("tmp/cert.pem")
				os.system("rm -rf tmp")
			elif options.pem:
				pinner(options.pem)
		else:
			print (sys.argv[0] + " --help")
except:
	pass

	
