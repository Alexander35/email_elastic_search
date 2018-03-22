import imaplib
import datetime
from django.conf import settings

def imap_connect():

	try:
		mail = imaplib.IMAP4_SSL(settings.IMAP4_SSL)
		mail.login(settings.TARGET_MAIL, settings.TARGET_MAIL_PASS)
		mail.list()
		return mail
	except	Exception as exc:
		print('unable to connect to the mailbox : {}'.format(exc))
		return None 

def fetch_all_new_ids_from_inbox(mail):

	if mail == None:
		return None
	try:	
		mail.select("inbox") # connect to inbox.

		result, data = mail.uid('search', None, '(UNSEEN)')
		print(result , data)
		 
		ids = data[0] # data is a list.

		print('ids {}'.format(ids))

		id_list = ids.split() # ids is a space separated string

		print('id_list {}'.format(id_list))



		# latest_email_id = id_list[-1] # get the latest

		# print('lastest_email_id {}'.format(latest_email_id))

		# result, data = mail.uid('fetch', latest_email_id, '(RFC822)')

		# print(result , data) 

		# raw_email = data[0][0]

		# print(raw_email.decode('utf-8'))	

		return id_list
	except Exception as exc:
		print('Unable to fetch the data from the mailbox : {}'.format(exc))	

def save_mails(ids_list):
	pass		