from django.urls import path
from .views import info_page_view


urlpatterns = [
    path('info_page/', info_page_view),
]