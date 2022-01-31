from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="warszawa1-index")
]