# dwitter/urls.py
from django.urls import include,path
from dwitter.views import dashboard,profile_list,profile



urlpatterns = [

 path("dashboard/", dashboard, name="dashboard"),
 path("profile_list/", profile_list, name="profile_list"),
 path("profile/<int:pk>", profile, name="profile"),
 path("accounts/", include("django.contrib.auth.urls")),
]