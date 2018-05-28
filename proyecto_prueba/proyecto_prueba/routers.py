from rest_framework import routers
from prueba.views import MiVistaSet


router=routers.DefaultRouter()
#REGISTRO MI VISTA (API) PERO COMO NO TENGO UN MODELO  LE PONGO EL BASE_NAME
router.register(r'prueba',MiVistaSet,base_name='lista')
urlpatterns = router.urls 