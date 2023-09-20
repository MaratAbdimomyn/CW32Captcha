from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListPlanet.as_view(), name='home'),
    path('create/', CreatePlanet.as_view(), name='create'),
    path('captcha/', include('captcha.urls'))
]