from rest_framework import routers
from .api import HostViewSet, TravelerViewSet, TripViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('api/hosts', HostViewSet, 'hosts')
router.register('api/travelers', TravelerViewSet, 'travelers')
router.register('api/trips', TripViewSet, 'trips')
router.register('api/reviews', ReviewViewSet, 'reviews')

urlpatterns = router.urls
