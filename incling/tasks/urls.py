from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet, 'tasks')
router.register('api/tiles', TileViewSet, 'tiles')

urlpatterns = router.urls