from django.conf.urls import url

from . import views

app_name='calendarPage'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
   
]
