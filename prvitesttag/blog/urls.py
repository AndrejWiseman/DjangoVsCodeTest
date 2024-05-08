from django.urls import path
from .views import home, detail_view, tagged

urlpatterns = [
    path('', home, name='home'),
    path('post/<slug:slug>/', detail_view, name="detail"),
    path('tag/<slug:slug>/', tagged, name="tagged"),

]