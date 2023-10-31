from django.urls import include, path

app_name = "api"
urlpatterns = [path("", include("my_awesome_project.core.urls"))]
