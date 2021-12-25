from django.urls import path
from system_prescription import views


app_name = "prescription"
urlpatterns = [
    path('new_prescription/', views.new_prescription, name='new_prescription'),
    path('get_patient_prescriptions/', views.get_patient_prescriptions, name='get_patient_prescriptions'),
    path('get_doctor_prescriptions/', views.get_doctor_prescriptions, name='get_doctor_prescriptions'),
    path('get_admin_prescriptions/', views.get_admin_prescriptions, name='get_admin_prescriptions'),
    path('get_number_of_new_prescriptions/', views.get_number_of_new_prescriptions, name='get_number_of_new_prescriptions')
]
