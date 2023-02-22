from django.urls import re_path
from app.views import IndexView

app_name = 'app'

urlpatterns = [
    re_path(r'^', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/', IndexView.as_view(), name='index'),
]
