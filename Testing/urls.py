from django.contrib import admin
from django.urls import path, include
from .router import router
#from rest_framework.urlpatterns import format_suffix_patterns
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Api.urls')),
    path('api/', include(router.urls)),
    #path('api/', views.Pizzalist.as_view()),

]
#urlpatterns = format_suffix_patterns(urlpatterns)
