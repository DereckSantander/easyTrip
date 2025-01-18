from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    ITINERARY_STATUS = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADO', 'Completado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="itineraries")
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=100)
    duration = models.IntegerField()
    num_people = models.IntegerField()
    status = models.CharField(max_length=10, choices=ITINERARY_STATUS, default='PENDIENTE')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f"Itinerary to {self.destination} by {self.user.name}"
    
class Package(models.Model):
    PACKAGE_TYPE_CHOICES = [
        ('Green', 'Green Package'),
        ('Regular', 'Regular Package'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    package_type = models.CharField(max_length=10, choices=PACKAGE_TYPE_CHOICES, default='Regular')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['package_type']

    def __str__(self):
        return f"{self.get_package_type_display()} - {self.name}"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="reservations")
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.name} for {self.package.name}"

class Payment(models.Model):
    payment_status = [
        ('SUCCESSFUL', 'Successful'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=payment_status)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.name}"

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="surveys")
    rating = models.PositiveIntegerField()  # Scale 1 to 5
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey by {self.user.name} with rating {self.rating}"