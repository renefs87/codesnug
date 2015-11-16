from registration.views import RegistrationView


class Home(RegistrationView):

    template_name = 'home.html'
    success_url = '/accounts/register/complete/'
    #form_class = UserRegistrationForm