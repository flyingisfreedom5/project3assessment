from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateWish.as_view(),  name='add_wish'),
    path('delete/<int:pk>', views.DeleteWish.as_view(), name='delete_wish'),
]