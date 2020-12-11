from Api.viewsets import PizzaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Pizza', PizzaViewset)
