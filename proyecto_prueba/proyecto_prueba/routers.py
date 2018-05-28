from rest_framework import routers
from prueba.views import MiVista

router=routers.DefaultRouter()
router.register(r'prueba',MiVista,base_name='lista')
urlpatterns = router.urls 