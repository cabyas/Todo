from django.urls import path

from todo.views import HelloView, hello_page

urlpatterns = [
    path('', HelloView.as_view(), name='hello'),
]