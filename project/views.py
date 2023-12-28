from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
    
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def annapurna(request):
    return render(request,'an.html')

def esa(request):
    return render(request, 'ES.html')

def jai(request):
    return render(request,'jai.html') 

def resume(request):
    return render(request,'pdf.html')
def contact(request):
    return render(request,'contact.html')

def mail(request): 
    subject = str(request.POST["subject_1"])
    name= str(request.POST["name1"])
    email = str(request.POST["email_id1"])
    mmsg = str(request.POST["msg"])
    mess = f"Name: {name}\nEmail: {email}\n\nMessage: {mmsg}"
    recipient_list = ['kirankumarr1901@gmail.com'] # List of recipient email addresses
    messages.success(request,'The Message Send. Please Wait We Will Get to You in a Short While')
    send_mail(subject, mess, 'kirankumarr1901@gmail.com',recipient_list, fail_silently=False)
    

    return redirect('contact')
  