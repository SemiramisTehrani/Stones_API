# created by Semi

from django.urls import path
from . import views

urlpatterns = [
    path('', views.stones_list),
    # path('<int:pk>/' , views.stone_detail),
]

