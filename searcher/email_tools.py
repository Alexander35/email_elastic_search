import imaplib
import datetime
from django.conf import settings
import email
from email.header import decode_header
from .models import Email
import quopri


class EmailTool():

	def __init__(self):
		self.imap_connect()

	def fetch_new_and_save(self):
		ids_list = self.fetch_all_new_ids_from_inbox()
		emails = self.get_mails(ids_list)
		savedmails = [ self.save_mail(email) for email in emails ]
		return savedmails

	def imap_connect(self):

		try:
			self.mail = imaplib.IMAP4_SSL(settings.IMAP4_SSL)
			self.mail.login(settings.TARGET_MAIL, settings.TARGET_MAIL_PASS)
			self.mail.list()
			# return self.mail
		except	Exception as exc:
			print('unable to connect to the mailbox : {}'.format(exc))
			return None 

	def fetch_all_new_ids_from_inbox(self):

		if self.mail == None:
			return None
		try:	
			self.mail.select("inbox") # connect to inbox.

			result, data = self.mail.uid('search', None, '(UNSEEN)')
			ids = data[0] # data is a list.
			id_list = ids.split() # ids is a space separated string

			return id_list
		except Exception as exc:
			print('Unable to fetch the data from the mailbox : {}'.format(exc))	

	def get_one_mail(self, email_id):
		_, data = self.mail.uid('fetch', email_id, '(RFC822)')
		_, mail = data[0]
		msg = email.message_from_string(mail.decode('utf-8', 'backslashreplace'))

		print(msg['From'])

		return [mail.decode(), msg] 

	def get_mails(self, ids_list):
		emails = [ self.get_one_mail(email_id) for email_id in ids_list ]
		# print(emails)
		return emails

	def save_mail(self, email):
		[(subj, code)] = decode_header(email[1]['Subject'])

		new_email = Email(
				title=subj.decode(code),
				sender=email[1]['From'],
				date=email[1]['Date'],
				text= quopri.decodestring(email[0].encode('utf-8')).decode('utf-8', 'backslashreplace')
			)
		new_email.save()

		return new_email