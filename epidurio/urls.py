from django.conf.urls import include, url
from opal.urls import urlpatterns as opatterns
from django.contrib import admin
from epidurio import api

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'fhir/v0.1/', include(api.epidurio_router.urls)),
]

urlpatterns += opatterns
