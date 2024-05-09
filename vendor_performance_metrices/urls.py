from django.urls import path
from . import views

app_name = 'vendor_performance_metrices'

urlpatterns = [
     path('metrices_api/', views.PerformanceView.as_view({'get': 'list'}), name='performance'),

]
