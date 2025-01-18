from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import User, Itinerary, Package, Reservation, Payment, Survey
from .serializers import UserSerializer, ItinerarySerializer, PackageSerializer, ReservationSerializer, PaymentSerializer, SurveySerializer
from .utils import export_to_csv

class user_list(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class itinerary_list(generics.ListCreateAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

class itinerary_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

class package_list(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class package_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class reservation_list(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class reservation_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class payment_list(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class payment_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class survey_list(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class survey_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


# Exportar Usuarios
def export_users_csv(request):
    fields = ['id', 'name', 'email']
    queryset = User.objects.all()
    return export_to_csv(queryset, 'users', fields)

# Exportar Paquetes
def export_packages_csv(request):
    fields = ['id', 'name', 'description', 'price', 'availability', 'package_type']
    queryset = Package.objects.all()
    return export_to_csv(queryset, 'packages', fields)

# Exportar Reservas con el nombre del usuario y nombre del paquete
def export_reservations_csv(request):
    fields = ['id', 'reservation_date']  # Campos directos
    related_fields = {
        'user': 'name',  # Campo relacionado: Mostrar el nombre del usuario
        'package': 'name',  # Campo relacionado: Mostrar el nombre del paquete
    }
    queryset = Reservation.objects.all()
    return export_to_csv(queryset, 'reservations', fields, related_fields)

# Exportar Itinerarios con el nombre del usuario
def export_itineraries_csv(request):
    fields = ['id', 'budget', 'destination', 'duration', 'num_people', 'status']
    related_fields = {
        'user': 'name',  # Campo relacionado: Mostrar el nombre del usuario
    }
    queryset = Itinerary.objects.all()
    return export_to_csv(queryset, 'itineraries', fields, related_fields)

# Exportar Pagos con el nombre del usuario
def export_payments_csv(request):
    fields = ['id', 'amount', 'payment_method', 'status']
    related_fields = {
        'user': 'name',  # Campo relacionado: Mostrar el nombre del usuario
    }
    queryset = Payment.objects.all()
    return export_to_csv(queryset, 'payments', fields, related_fields)

# Exportar Encuestas
def export_surveys_csv(request):
    fields = ['id', 'rating', 'comments']
    related_fields = {
        'user': 'name',  # Campo relacionado: Mostrar el nombre del usuario
    }
    queryset = Survey.objects.all()
    return export_to_csv(queryset, 'surveys', fields, related_fields)