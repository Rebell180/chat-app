from django.urls import path, include
from .views import ChatView

urlpatterns = [
    path('api/chat/', ChatView.as_view(), name="chat"),
]