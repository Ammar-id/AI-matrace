from django.conf.urls import url
from django.urls import path, include
from .views import (
    ArticleListApiView,
    CarrierListApiView,
)

urlpatterns = [
    path('articles', ArticleListApiView.as_view()),
    path('carriers', CarrierListApiView.as_view()),
]