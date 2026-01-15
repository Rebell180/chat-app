from django.urls import path, include
from .api import views

urlpatterns = [
    path('', include('chat_app.api.urls')),
]