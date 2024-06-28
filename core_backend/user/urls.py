from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset import UserViewSet


app_name = 'user'
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = router.urls

# urlpatterns = [
#     # *router.urls,
#     path('user/', UserViewSet.as_view({'get':'list'}), name='user'),
#     path('user/<uuid:pk>/', UserViewSet.as_view({'get':'retrieve'}), name='user-id'), 
# ]




