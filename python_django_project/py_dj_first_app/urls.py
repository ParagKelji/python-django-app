from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="Contact")
]

urlpatterns += staticfiles_urlpatterns()