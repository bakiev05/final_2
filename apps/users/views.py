from apps.users.models import User
# from apps.users.forms import UserRegistrationForm
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
# from django.views.generic import CreateView
# from django.urls import reverse_lazy


# class UserCreateView(CreateView):
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})