import random
from faker import Faker
from .models import User, Package, Reservation, Itinerary, Payment, Survey

fake = Faker()

# Configuración: número de usuarios
NUM_USERS = 50

# Generar Usuarios
def create_users(n=NUM_USERS):
    users = []
    for _ in range(n):
        users.append(User(
            name=fake.name(),
            email=fake.unique.email(),
            password=fake.password(length=10),
        ))
    User.objects.bulk_create(users)
    print(f"{n} usuarios creados.")

# Generar Paquetes
def create_packages(n=None):
    if n is None:
        n = NUM_USERS * 2  # Doble del número de usuarios
    package_types = ['Green', 'Regular']
    packages = []
    for _ in range(n):
        packages.append(Package(
            name=fake.catch_phrase(),
            description=fake.text(max_nb_chars=200),
            price=round(random.uniform(50.0, 1000.0), 2),
            availability=random.choice([True, False]),
            package_type=random.choice(package_types),
        ))
    Package.objects.bulk_create(packages)
    print(f"{n} paquetes creados.")

# Generar Reservas
def create_reservations(n=None):
    if n is None:
        n = NUM_USERS * 1.5  # Una y media veces el número de usuarios
    users = list(User.objects.all())
    packages = list(Package.objects.all())
    reservations = []
    for _ in range(int(n)):
        reservations.append(Reservation(
            user=random.choice(users),
            package=random.choice(packages),
        ))
    Reservation.objects.bulk_create(reservations)
    print(f"{int(n)} reservas creadas.")

# Generar Itinerarios
def create_itineraries(n=None):
    if n is None:
        n = NUM_USERS * 2  # Doble del número de usuarios
    users = list(User.objects.all())
    itineraries = []
    statuses = ['Pending', 'Completed']
    for _ in range(n):
        itineraries.append(Itinerary(
            user=random.choice(users),
            budget=round(random.uniform(500.0, 5000.0), 2),
            destination=fake.city(),
            duration=random.randint(1, 14),  # Duración en días
            num_people=random.randint(1, 10),
            status=random.choice(statuses),
        ))
    Itinerary.objects.bulk_create(itineraries)
    print(f"{n} itinerarios creados.")

# Generar Pagos
def create_payments(n=None):
    if n is None:
        n = NUM_USERS * 2  # Doble del número de usuarios
    users = list(User.objects.all())
    payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer']
    statuses = ['Successful', 'Failed']
    payments = []
    for _ in range(n):
        payments.append(Payment(
            user=random.choice(users),
            amount=round(random.uniform(10.0, 1000.0), 2),
            payment_method=random.choice(payment_methods),
            status=random.choice(statuses),
        ))
    Payment.objects.bulk_create(payments)
    print(f"{n} pagos creados.")

# Generar Encuestas
def create_surveys(n=None):
    if n is None:
        n = NUM_USERS  # Igual al número de usuarios
    users = list(User.objects.all())
    surveys = []
    for _ in range(n):
        surveys.append(Survey(
            user=random.choice(users),
            rating=random.randint(1, 5),
            comments=fake.text(max_nb_chars=200),
        ))
    Survey.objects.bulk_create(surveys)
    print(f"{n} encuestas creadas.")

# Llenar la Base de Datos
def populate_database():
    create_users(NUM_USERS)
    create_packages()
    create_reservations()
    create_itineraries()
    create_payments()
    create_surveys()

# Ejecutar la población de datos
populate_database()
