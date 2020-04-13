from django.urls import path, include

from applications.accounts import views

urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name="login"),
    path('auth/password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', views.RegisterView.as_view(), name="register"),
]
