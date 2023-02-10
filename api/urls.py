from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'teammembers', views.TeamMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('teammembers/', views.TeamMemberListView.as_view()),
    # path('teammembers/<int:pk>', views.TeamMemberDetailView.as_view()),edit_teammember_form
    path('teammembers/<int:pk>', views.edit_teammember_form),
    path('teammembers/add', views.add_teammember_form)
]