from django.conf import settings
from django.db import models


class UserMixin(models.Models):
    user = models.ForeignKey (
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="User",
        help_text="",
    )

    class Meta:
        abstract = True
    # Nie jest to faktyczny user - tylko abstrakcyjny,
    # django próbowałoby stworzyc tabelke user

class Category(UserMixin, models.Model):
    name = models.CharField(
    max_length = 50,
    null=False,
    blank = False,
    verbose_name="Name",
    help_text="",
    )
    # sposob uzycia tekstu lukasz-jemiol
    slug = models.SlugField()

    description = models.CharField (
        max_length = 150,
        null=False,
        blank=True,
        # Opcja Django
        default="",
        verbose_name="Descritpion",
        help_text="",
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        help_text="",
    )
    # user = models.ForeignKey (
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT,
    #     null=False,
    #     blank=False,
    #     verbose_name="User",
    #     help_text="",
    # )----- userMixin


class Plant (UserMixin, models.Model):
    name = models.CharField(
        max_length = 50,
        null=False,
        blank = False,
        verbose_name="Name",
        help_text="",
    )
    category = models.ForeignKey (
        Category,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Category",
        help_text="",
    )

    watering_interval = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name = "Watering interval",
        help_text = "In seconds",
        # zeby szybciej testowac funkcjon
    )
    fertilizing_interval = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name = "Fertilizing interval",
        help_text = "In seconds",
        # zeby szybciej testowac funkcjon
    )

    required_exposure = models.CharField (
        max_length=10,
        choices=EXPOSURE_CHOICES,
        null=False,
        blank=False,
        verbose_name="Amount of sun",
        help_text="",
    )
#   EXPOSURE_CHOICES = [ ("elem", "opis tego elem")] choises
    EXPOSURE_CHOICES = [ ("dark", "Dark"),
    ("shade","Shade"),
    ("partsun", "Part sun"),
    ("fullsun", "Full sun"),
    ]

    required_humidity = models.CharField (
        max_length=10,
        choices=HUMIDITY_CHOICES,,
        null=False,
        blank=False,
        verbose_name="Humidity",
        help_text="",
    )
    HUMIDITY_CHOICES = [ ("low", "Low"),
    ("medium","Medium"),
    ("high", "High"),
    ]
    required_temperature = models.CharField (
        max_length=10,
        choices=TEMPERATURE_CHOICES,
        null=False,
        blank=False,
        verbose_name="Temperature",
        help_text="",
    )
    TEMPERATURE_CHOICES = [ ("cold", "Cold"),
    ("medium","Medium"),
    ("warm", "Warm"),
    ]

    blooming = models.BooleanField(
        default=False,
        # default musi byc ustawiony bo pola niżej mogą być bez wartości
        null=False,
        blank=True,
        # zgoda na przesłanie pustego form
        verbose_name = "Blooming?"
    )

    dificulty = models.PositiveIntegerField (
        choices = DIFICULTY_CHOICES,
        default=1,
        null=False,
        blank=True,
        verbose_name="Cultivation difficulty level",
        help_text = "",

    )

    DIFICULTY_CHOICES = [
        (1, "Low"),
        (2, "Medium-low"),
        (3, "Medium"),
        (4, "Medium-high"),
        (5, "High"),
    ]
    # user = models.ForeignKey (
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT,
    #     null=False,
    #     blank=False,
    #     verbose_name="User",
    #     help_text="",
    # )----- userMixin
class Room(UserMixin, models.Model):
    name = models.CharField(
        max_length = 50,
        null=False,
        blank = False,
        verbose_name="Room_name",
        help_text="",
    )



      room_exposure = models.CharField (
        max_length = 20,
        choices = ROOMEXPOSURE_CHOICES,
        null=False,
        blank=False,
        verbose_name="Room exposure",
        help_text="",
    )
    ROOMEXPOSURE_CHOICES = [ ("dark", "Dark room"),
    ("shade","Shady room"),
    ("partsun", "Partsunny room"),
    ("fullsun", "Sunny room"),
    ]
    room_temperature = models.CharField (
        max_length = 20,
        choices = ROOMTEMP_CHOICES,
        null=False,
        blank=False,
        verbose_name = "Room temperature",
        help_text = "",
    )
    ROOMTEMP_CHOICES = [ ("cold", "Cold"),
    ("medium","Medium"),
    ("warm", "Warm"),
    ]


    aeration = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name = "Aeration"
    )


class UserPlant(Plant,models.Model):
    name = models.CharField(
        max_length = 50,
        null=False,
        blank = False,
        verbose_name="Plant_name",
        help_text="",
    )

    room = models.ForeignKey (
        Room,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Room",
        help_text="",
    )
    plant = models.ForeignKey (
        Room,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name=" Plant origin",
        help_text="",
    )


    description=models.TextField(
        blank=True,
        verbose_name = "Description",
        help_text="",
        )

     watering_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Watering date",
        help_text="",
        )

        fertilizing_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Fertilizing date",
        help_text="",
        )



