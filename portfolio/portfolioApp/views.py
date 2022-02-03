from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from portfolio import settings
# Create your views here.
    

def home(request):
    return render(request, 'portfolio/home.html')


def aboutme(request):
    return render(request, 'portfolio/about-me.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):

    if request.method == 'POST':
        print("posteo")

        subject = request.POST['Nombre'] + ' ' +request.POST['apellido']
        message = request.POST['msg']           
        mail= request.POST['emailInfo']  
        phone= request.POST['phoneNumber']  

        #asunto = nombre + " " + apellido
        #contenido =  email + " " + phoneNumber + " " + msg
        email_from= settings.EMAIL_HOST_USER
        recipient_list=['lonzofrancisco@gmail.com']
        header = "MAIL DESDE PORTAFOLIO!!" + ' '+ mail
        message = "Hola soy: " + subject +  ' Mi numero es: ' + phone + "\n" + 'Mensaje: '+ message
        send_mail(header,message,email_from,recipient_list)





    return render(request, 'portfolio/contact.html')