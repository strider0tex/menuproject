from django.urls import path
from menu.views import MenuView

#comment

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]