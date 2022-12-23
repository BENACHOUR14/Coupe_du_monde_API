from rest_framework import routers
from Teams import views

router = routers.DefaultRouter()
router.register(r'Teams', views.TeamViewSet)
