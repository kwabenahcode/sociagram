from django.urls import path
from rest_framework.routers import DefaultRouter
from usersauth.viewsets.register import *

app_name = 'usersauth'
router = DefaultRouter()
router.register(r'auth/register', RegisterUserViewSet, basename='register' )

urlpatterns = router.urls

# urlpatterns=[
#     path('auth/register', )
# ]