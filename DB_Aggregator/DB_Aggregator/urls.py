from django.contrib import admin
from django.urls import path
from DB_Aggregator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_patient_prescriptions/', views.list_patient_prescriptions, name='list_patient_prescriptions'),
    path('list_doctor_prescriptions/', views.list_doctor_prescriptions, name='list_doctor_prescriptions'),
    path('list_prescriptions/', views.list_prescriptions, name='list_prescriptions'),
    path('list_doctors/', views.list_doctors, name='list_doctors'),
    path('list_patients/', views.list_patients, name='list_patients'),
    path('get_daily_statistics/', views.get_daily_statistics, name='get_daily_statistics')
]
