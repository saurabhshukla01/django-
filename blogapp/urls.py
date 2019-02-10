from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('login/',login_user,name='log'),
	path('logout/',logout_user,name='logout'),
	path('changepass/',changepassword,name='changepass'),
]