from django.urls import path
from .views import DataPageView, HomePageView, DataCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', DataCreateView.as_view(), name='data_new'),
    path('data_detail/', DataPageView.as_view(), name='data_detail')
]