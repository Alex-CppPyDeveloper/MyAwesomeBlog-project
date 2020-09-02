from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.schowblog, name='schowblog'),
	path('<int:post_id>/', views.specific_post, name='specific_post'),
]