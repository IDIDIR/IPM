# import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as PKCS1_OAEP
from base64 import b64decode,b64encode

# class ComingSoon():
# 	def __init__(self):
# 		pass()

def main():
	undefined = list() # use class of array until it became a mainstream
	# with open("./temp_pk.txt", "r", encoding="utf8") as public_key:
	# 	print( public_key.read() )
	# with open("./temp_em.txt", "r", encoding="utf8") as encoded_message:
	# 	print( encoded_message.read() )

	## AICC is a company that has been working from time immemorial
	#  when the RAM in the PC was barely enough for the consoled chrome
	#  so among the deadly sins in their corporate RFC is
	## print(bro, please add a fun about vars and glutteny")

	message = b"foo bazat blahblah"
	public_key = "./keys/bazad1/public.pem"
	private_key = "./keys/bazad1/private.pem"
	#
	public_key = open(public_key,"r").read()
	public_key = RSA.importKey(public_key)
	public_key = PKCS1_OAEP.new(public_key)
	message = public_key.encrypt(message)			# 1
	message = b64encode(message)				# 2
	print(message)
	private_key = open(private_key,"r").read()
	private_key = RSA.importKey(private_key)
	private_key = PKCS1_OAEP.new(private_key)
	message = b64decode(message)				# 2
	message = private_key.decrypt(message)			# 1
	print(message)

if __name__ == '__main__':
	main()
