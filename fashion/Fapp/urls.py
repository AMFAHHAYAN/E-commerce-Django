from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPage.as_view(),name="index"),   
    path('login/', Login.as_view(),name="login"), 
    path('signup/', Signup.as_view(),name="signup"),
    path('forget/', Forget.as_view(),name="forget"),
    path('reset/<uuid:uuid>', Reset.as_view(),name="reset"),
    path('dashboard/', Dashboard.as_view(),name="dashboard"),
    path('dashboard/login/', errorPage.as_view(),name="error"),
    path('detail/', Detail.as_view(),name="detail"),
    path('logout/', Logout.as_view(),name="logout"),
]
