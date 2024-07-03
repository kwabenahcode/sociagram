from django.urls import path
from rest_framework.routers import DefaultRouter
from usersauth.viewsets.register import *
from usersauth.viewsets.login import *

app_name = 'usersauth'

router = DefaultRouter()
router.register(r'auth/register', RegisterUserViewSet, basename='register' )


urlpatterns=[
    path('auth/login/', LoginViewSet.as_view({'post':'login'}) )
]

urlpatterns += router.urls