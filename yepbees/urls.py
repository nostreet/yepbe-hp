
from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name="home"),
    url(r"^about/$", TemplateView.as_view(template_name="about.html"),
        name="about"),
    url(r"^products/$", TemplateView.as_view(template_name="products.html"),
        name="products"),
    url(r"^faqs/$", TemplateView.as_view(template_name="faqs.html"),
        name="faqs"),
    url(r"^contact/$", views.emailView,
        name="contact"),
    url(r"^tandcs/$", TemplateView.as_view(template_name="tandcs.html"),
        name="tandcs"),


]
