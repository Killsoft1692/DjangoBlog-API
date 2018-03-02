from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import User
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View


class RegistrationFormView(View):
    form_class = RegisterForm
    template_name = 'accounts/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password2')
            user.set_password(password)
            user.save()
            from_email = settings.EMAIL_HOST_USER
            recipient = [form.data['email']]
            html_mail_part = "<h1>Activation</h1><a href=http://{}/activate/{}>Activate your account</a>".format(
                request.META['HTTP_HOST'], user.id)
            msg = EmailMultiAlternatives(
                'Thank you for register',
                'Please Activate your account',
                from_email,
                recipient,
            )
            msg.attach_alternative(html_mail_part, 'text/html')
            msg.send()

            return render(request, 'accounts/waiting_activation.html', {'name': name})

        return render(request, self.template_name, {
            'form': form
        })


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'accounts/login_form.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            email = form.data['email']
            password = form.data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

            else:
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form})

        return HttpResponse('First activate your account')


def activate_user(request, id_):
    user = User.objects.get(pk=int(id_))
    if user:
        user.set_active
        user.save()

        return redirect('accounts:login')


def logout_view(request):
    logout(request)

    return redirect('/')
