from django.urls import path
from .import views
urlpatterns = [
    path("post/",views.PersonRegisterPostView.as_view()),
    path("get/",views.PersonRegisterGetView.as_view())
    
]