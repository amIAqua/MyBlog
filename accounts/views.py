from django.shortcuts import render, reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.http import HttpResponseRedirect

def SignupView(request):

    template_name = 'accounts/sign_up.html'

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(

                    username = username,
                    password = password
                )

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('blog:MainPageView'))
        
        else:
            messages.info(request, 'Wrong data')    
            return HttpResponseRedirect(reverse('accounts:SignupView'))

    else:
        return render(request, template_name)


def Registration(request):

    template_name = 'accounts/registration.html'

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        

        if password == password_confirm:



            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username is already taken')
                return HttpResponseRedirect(reverse('accounts:Registration'))

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email is already exists')
                return HttpResponseRedirect(reverse('accounts:Registration'))

            else:
                user = User.objects.create_user(

            		first_name = first_name,
            		last_name = last_name,
            		username = username,
            		password = password,
            		email = email
                )
               
                user.save()
                return HttpResponseRedirect(reverse('accounts:SignupView'))

        else:
        	messages.info(request, 'Password is not matching')
        	return HttpResponseRedirect(reverse('accounts:Registration'))
    
    else:
    	return render(request, template_name)


def SignoutView(request):

    auth.logout(request)
    return HttpResponseRedirect('/')









    
