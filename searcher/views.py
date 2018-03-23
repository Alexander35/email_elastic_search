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

	ET = EmailTool()
	saved_mails = ET.fetch_new_and_save()

	return render(
		request,
		'new_mails_list.html',
		{
			'title' : 'New Mails List',
			'saved_mails' : saved_mails
		}
    )    