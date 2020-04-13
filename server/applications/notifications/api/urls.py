from django.urls import path

from applications.notifications.api.views import NotificationListView

urlpatterns = [
    path(
        'notifications/',
        NotificationListView.as_view(),
        name="notification-list",
    ),
]
