from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .email_tools import *

@login_required
def main(request):

	mail = imap_connect()
	ids_list = fetch_all_new_ids_from_inbox(mail)
	

	return render(
		request,
		'main.html',
		{
			'title' : 'Get Unreaded Emails'

		}
    )