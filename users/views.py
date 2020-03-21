from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def logout_view(request):
	"""Log out the user."""
	logout(request)
	return HttpResponseRedirect(reverse('journals:index'))
	#return render(request, 'journals/index.html')


def register(request):
	"""Register users."""
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(request.POST)
		# two password matching validation is done in UserCreationForm

		if form.is_valid():
			# new_user is a django.contrib.auth.models.User object
			new_user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			authenticated_user = authenticate(
				username=username,
				password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('users:login'))

	context = {'form':form}
	return render(request, 'users/register.html', context)
