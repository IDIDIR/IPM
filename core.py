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


	# send public_2 over GitHub (recipient)
	public_file = "./keys/bazad2/public.pem"
	public_key = open(public_file,"r").read()
	tag_KEYS = "./temp_pk.txt"
	open(tag_KEYS,"w").write(public_key)
	# encrypt message with public_2 (sender)
	public_file = "./temp_pk.txt"
	public_key = open(public_file,"r").read()
	public_key = RSA.importKey(public_key)
	public_key = PKCS1_OAEP.new(public_key)
	message = "foo bazat blahblah"
	message = message.encode('utf-8')
	message = public_key.encrypt(message)			# 1
	message = b64encode(message)							# 2
	tag_PM = "./temp_em.txt"
	open(tag_PM,"w").write(message.decode('utf-8'))
	# decrypt message with private_2 (recipient)
	private_key = "./keys/bazad2/private.pem"
	private_file = open(private_key,"r").read()
	private_key = RSA.importKey(private_file)
	private_key = PKCS1_OAEP.new(private_key)
	message = b64decode(message)							# 2
	message = private_key.decrypt(message)		# 1
	print(message.decode('utf-8'))


if __name__ == '__main__':
	main()
