from rest_framework import routers
from Games import views

router = routers.DefaultRouter()
router.register(r'Games', views.GameViewSet)
