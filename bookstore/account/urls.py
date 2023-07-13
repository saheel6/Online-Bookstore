from django.urls import path
from .views import Signupview,Logout


urlpatterns = [

    
       path('signupu',Signupview.as_view(),name='Signupu'),
       path('logout',Logout.as_view(),name='logout')

    

]