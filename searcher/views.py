from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .email_tools import *

@login_required
def main(request):



	return render(
		request,
		'main.html',
		{
			'title' : 'Get Unreaded Emails'

		}
    )

@login_required
def new_mails_list(request):

	mail = imap_connect()
	ids_list = fetch_all_new_ids_from_inbox(mail)
	

	return render(
		request,
		'new_mails_list.html',
		{
			'title' : 'New Mails List'

		}
    )    