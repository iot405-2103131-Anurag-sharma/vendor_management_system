from django.urls import path
from . import views

app_name = 'purchase_order'

urlpatterns = [
     path('purchase_api/', views.PurchaseOrderView.as_view({'get': 'list', }), name='purchase'),
     path('api/<int:vendorid>/', views.PurchaseOrderView.as_view({'get': 'list', }), name='purchase'),

]
