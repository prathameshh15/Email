from django.urls import path
from emails import views

urlpatterns = [
    path('ulogin',views.ulogin),
    path('otp/<rid>',views.eotp),
    path('msg',views.msg),
]