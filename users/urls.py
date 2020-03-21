"""Define URL patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
	# Login page
	# using django existing view login
	url(r'^login/$', 
		LoginView.as_view(template_name='users/login.html'),
		name='login'),
	# Logout page
	url(r'^logout/$',views.logout_view, name='logout'),
	url(r'^register/$',views.register, name='register'),
]