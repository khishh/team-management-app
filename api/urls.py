from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'teammembers', views.TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('datetime/', views.current_datetime),
    path('teammembers/list', views.TeamMemberListView.as_view())
]