from .views import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("note",NoteViewSet,basename="note")

urlpatterns = router.urls