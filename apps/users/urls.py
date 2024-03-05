
from .views import UserViewset, VerificationViewset
from rest_framework import routers

router = routers.DefaultRouter()

# routes for user model
router.register(r'user', UserViewset)
router.register(r'verification', VerificationViewset)

urlpatterns = router.urls