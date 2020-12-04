from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
from .views import *


urlpatterns = [
    path('auth/login/', Login.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/token-refresh/', refresh_jwt_token),
    path('registration/', include('rest_auth.registration.urls')),
]

router = routers.DefaultRouter()
router.register('user',  UserViewSet, basename='user')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns+= router.urls

