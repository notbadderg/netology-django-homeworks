from django.urls import path

from measurement.views import SensorsListView, SensorView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsListView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementCreateView.as_view())
]










