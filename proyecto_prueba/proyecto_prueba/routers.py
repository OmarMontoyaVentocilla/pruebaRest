from rest_framework import routers
from prueba.views import MiVistaSet

router=routers.DefaultRouter()
router.register(r'prueba',MiVistaSet,base_name='lista')
urlpatterns = router.urls 