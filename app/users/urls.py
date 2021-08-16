from django.urls import path

from users import views

app_name = 'user'

urlpatterns = [
    path('api/user/create/', views.CreateUserView.as_view(), name='create'),
    path('api/user/token/', views.CreateTokenView.as_view(), name='token')
]
