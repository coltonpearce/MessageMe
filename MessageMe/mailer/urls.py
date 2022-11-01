#Colton Pearce
#I am creating a program and a website for my company. It will have three 
# pages and I will have all those routes created so they can be accessed
from django.urls import path
from .views import aboutPageView
from .views import indexPageView
from .views import contactPageView


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about/", aboutPageView, name = "about"),
    path("contact/<str:contact_name>/<str:contact_email>", contactPageView, name = "contact")
]
