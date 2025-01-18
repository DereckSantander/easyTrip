from django.urls import path
from . import views

urlpatterns = [
    path('users',views.user_list.as_view(),name='user_list'),
    path('users/<int:pk>',views.user_detail.as_view(),name='user_detail'),
    path('itineraries',views.itinerary_list.as_view(),name='itinerary_list'),
    path('itineraries/<int:pk>',views.itinerary_detail.as_view(),name='itinerary_detail'),
    path('packages',views.package_list.as_view(),name='package_list'),
    path('packages/<int:pk>',views.package_detail.as_view(),name='package_detail'),
    path('reservations',views.reservation_list.as_view(),name='reservation_list'),
    path('reservations/<int:pk>',views.reservation_detail.as_view(),name='reservation_detail'),
    path('payments',views.payment_list.as_view(),name='payment_list'),
    path('payments/<int:pk>',views.payment_detail.as_view(),name='payment_detail'),
    path('surveys',views.survey_list.as_view(),name='survey_list'),
    path('surveys/<int:pk>',views.survey_detail.as_view(),name='survey_detail'),


    path('export/users/', views.export_users_csv, name='export_users_csv'),
    path('export/packages/', views.export_packages_csv, name='export_packages_csv'),
    path('export/reservations/', views.export_reservations_csv, name='export_reservations_csv'),
    path('export/itineraries/', views.export_itineraries_csv, name='export_itineraries_csv'),
    path('export/payments/', views.export_payments_csv, name='export_payments_csv'),
    path('export/surveys/', views.export_surveys_csv, name='export_surveys_csv'),
]
