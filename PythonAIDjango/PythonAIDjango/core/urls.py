from django.urls import path
from core.views import index

app_name = 'core'

urlpatterns = [
	# Add your URL patterns here
	path('', index, name='index'),
]

