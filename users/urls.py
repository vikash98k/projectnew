from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

router = DefaultRouter()
router.register('person',PersonViewSet,basename='person')


urlpatterns = [    
    path("post/",views.PersonRegisterPostView.as_view()),
    path("get/",views.PersonRegisterGetView.as_view()),
    path('details/',include(router.urls)),
    path('json/data/',views.PersonDataInputView.as_view())
]