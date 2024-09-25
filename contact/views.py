from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact_us(request):
    return render(request, 'contact.html')

def store_contact_us(request):
    # if request.method == 'POST':
    #     try:
    #         email = request.POST['email']
    #         subject = request.POST['subject']
    #         message = request.POST['message']
    #     except:
    #         return HttpResponse("Error")
        
    #     messages.success(request, 'Your message is submitted successfully!')
    #     return redirect('contact_us')
    # return HttpResponse(f"Congrats! Message is submitted having email:{email} and message:{message}" )


    # or

    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    Contact.objects.create(email=email,subject=subject,message=message)
    messages.success(request, 'Your message is submitted successfully!')
    return redirect('contact_us')