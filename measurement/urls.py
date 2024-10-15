from django.urls import path

from measurement.views import SensorMeasurementView, SensorDetail, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorMeasurementView.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),
    path('measurement/', MeasurementCreateView.as_view()),
]
