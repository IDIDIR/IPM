# import default libs
import os.path
import urllib.request
import json
from types import SimpleNamespace as Namespace # from argparse import Namespace
from base64 import b64decode,b64encode
# import additional libs
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as PKCS1_OAEP

## AICC is a company that has been working from time immemorial
#  when the RAM in the PC was barely enough for the consoled chrome
#  so among the deadly sins in their corporate RFC is
## print(bro, please add a fun about vars and glutteny")

# conf
access_token = ''

class messageList(list):
	def __init__(self):
		self = list()
	def add(self, name, text, date):
		self.append({
			'name': name,
			'text': text,
			'date': date
		})

# system magic
def json2obj(data): return json.loads(data, object_hook=lambda bazat: Namespace(**bazat))
# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def selfkey_exist():
	private_file 	= './keys/__self__/private.pem'
	return os.path.isfile(private_file)

def selfkey_generate():
	public_file 	= './keys/__self__/public.pem'
	private_file 	= './keys/__self__/private.pem'
	key = RSA.generate(2048)
	private_key = key.export_key()
	open(private_file, "wb").write(private_key)
	public_key = key.publickey().export_key()
	open(public_file, "wb").write(public_key)
	
def main():
	if (selfkey_exist()):
		mode = input('Post / Load: ')
		# switch case break foo bazat lorem ipsum
		if (mode == 'Post'): CreateMessage()
		if (mode == 'Load'): LoadMessages()
	else:
		print('Selfkeys don\'t found.\nGenerating.....')
		selfkey_generate()
		main()

def CreateMessage():
	# send public_2 over GitHub (recipient)
	message = input('Private message text: ')
	# secure encode
	eMessage = Encrypt(message)
	# github api write comment
	link = PostMessage(access_token, eMessage)
	print(link)
	
def LoadMessages():
	# github api parse comment
	eMessages = GetMessages(access_token)
	# decode in loop
	messages = messageList()
	{ messages.add(eMessage.user.login, Decrypt(eMessage.body), eMessage.created_at) for eMessage in eMessages }
	print(messages)

# 
def GetMessages(access_token):
	url = f'https://api.github.com/repos/IDIDIR/IPM/issues/3/comments?access_token={access_token}'
	req = urllib.request.Request(url)
	try: res = urllib.request.urlopen(req)
	except urllib.error.URLError as e:
		print(e.reason)
	return json2obj(res.read())
	# tmp = commentList(req.read())

#
def PostMessage(access_token, eMessage):
	url = f'https://api.github.com/repos/IDIDIR/IPM/issues/3/comments?access_token={access_token}'
	msg = json.dumps({"body": eMessage})
	msg = msg.encode('utf-8') 										# string to bytes
	req = urllib.request.Request(url, msg)
	try: res = urllib.request.urlopen(req)
	except urllib.error.URLError as e:
		print(e.reason)
	return 'oke'

# encrypt single message with public_2 (sender)
def Encrypt(message):
	public_file = "./keys/bazad2/public.pem"
	public_key = open(public_file,"r").read()
	public_key = RSA.importKey(public_key)
	public_key = PKCS1_OAEP.new(public_key)
	eMessage = message.encode('utf-8')						# 0
	eMessage = public_key.encrypt(eMessage)				# 1
	eMessage = b64encode(eMessage)								# 2
	eMessage = eMessage.decode('utf-8')						# ¯\_(ツ)_/¯
	return eMessage

# decrypt single message with private_2 (recipient)
def Decrypt(eMessage):
	private_key = "./keys/bazad2/private.pem"
	private_file = open(private_key,"r").read()
	private_key = RSA.importKey(private_file)
	private_key = PKCS1_OAEP.new(private_key)
	try:
		message = b64decode(eMessage)								# 2
		message = private_key.decrypt(message)			# 1
		message = message.decode('utf-8')						# 0
	except:
		message = f'! {eMessage}'
	return message

if __name__ == '__main__':
	main()


# class singleComment:
# 	def __init__(self, raw):
# 		self.text = raw['body']
# 		self.name = raw['user']['login']

# class commentList:
# 	def __init__(self, raws):
# 		self = json2obj(raws)

# tmp = {raw: singleComment(raw) for raw in tmp}
# tmp = {d.pop(singleComment(raw)) for raw in tmp}

# tag_PM = "./temp_em.txt"
# open(tag_PM,"w").write(message.decode('utf-8'))

# tag_KEYS = "./temp_pk.txt"
# open(tag_KEYS,"w").write(public_key)