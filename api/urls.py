from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'teammembers', views.TeamMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.TeamMemberListView.as_view()),
    # path('/', views.TeamMemberListView.as_view()),
    path('<int:pk>/edit', views.edit_teammember_form),
    path('add', views.add_teammember_form),
    path('<int:pk>/delete', views.delete_teammember)
]