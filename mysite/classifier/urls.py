from django.urls import path
from classifier.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]