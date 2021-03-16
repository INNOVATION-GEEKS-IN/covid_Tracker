
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import settings
from django.views.generic.base import RedirectView

from tracker import views as tracker_views 

# favicon view 
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('' , tracker_views.home ),
    path('tacker/', tracker_views.tracker),
    path('predict-Country/' , tracker_views.predict_Country ),
    path('admin/', admin.site.urls),
    path('contact_us/',tracker_views.contact_us ),
    path('compare/', tracker_views.compare ),
    path('vaccination/<int:id>/', tracker_views.vaccinations),
    path('vaccination/', tracker_views.vaccinations),
    path('vaccination-map/', TemplateView.as_view(template_name='index.html')),
    path('age-predict/', tracker_views.age_predict ),
    re_path(r'^favicon\.ico$', favicon_view),
] + staticfiles_urlpatterns()
