from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Itinerary)
admin.site.register(Package)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Survey)
