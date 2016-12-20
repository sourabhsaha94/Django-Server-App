
from django.shortcuts import render,redirect,render_to_response
from django_mailbox.models import Mailbox,Message
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MailStorage,Login
from .forms import RegisterForm,LoginForm
# Create your views here.

def details(request,pk):
	current_mailbox = Mailbox.objects.get(id=1)
	message_list = current_mailbox.get_new_mail()
	for msg in message_list:
		address_list = msg.from_address
		mail = MailStorage(sender=address_list[0],subject=msg.subject,body=msg.text,date=msg.processed)
		mail.save()

        username = Login.objects.get(pk=pk)
        mail_list = MailStorage.objects.filter(sender=username.username)
	context = {'current_mailbox' : current_mailbox,'email_list':mail_list}
	return render(request,'EmailArchiver/index.html',context)

def login(request):
        if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
                        try:
                                user = Login.objects.get(username=form.cleaned_data['username'])
                        except:
                                return redirect('index')
                        if(user.password == form.cleaned_data['password']):
                                return HttpResponseRedirect(reverse('details',args=(user.pk,)))

        else:
                form = LoginForm()
	return render(request,'EmailArchiver/login.html',{'form':form})

def register(request):
        if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                return redirect('index')
        else:
                form = RegisterForm()
	return render(request,'EmailArchiver/register.html',{'form':form})

