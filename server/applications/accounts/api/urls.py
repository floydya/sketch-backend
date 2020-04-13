from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from applications.accounts.api.views import UserViewSet, CurrentUserView, UserPasswordUpdateView

router = SimpleRouter()
router.register('users', UserViewSet, basename="users")

urlpatterns = router.urls + [
    path('auth/', include([
        path('login/', obtain_jwt_token),
        path('current/', CurrentUserView.as_view()),
        path('change-password/', UserPasswordUpdateView.as_view())
    ]))
]
