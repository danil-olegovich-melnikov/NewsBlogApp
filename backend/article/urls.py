from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'articles', views.ArticleViewSet)
urlpatterns = router.urls
