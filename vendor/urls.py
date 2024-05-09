from django.urls import path
from . import views

urlpatterns = [
     path('', views.VendorView.as_view({'get': 'list', 'post': 'create'}), name='vendor'),
    #  path('vendor/<int:id>/', views.VendorView.as_view({'get': 'list', }), name='vendor'),
]