from django.urls import path
from user.views import CustomTokenObtainPairView, UserView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/signup', UserView.as_view(), name='user_view'),
]
