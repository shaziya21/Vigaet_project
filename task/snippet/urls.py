from rest_framework.routers import DefaultRouter

from snippet.views import SearchView

router = DefaultRouter()
router.register("search", SearchView, basename="view_set_pre")
urlpatterns = router.urls
