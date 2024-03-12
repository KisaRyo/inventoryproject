from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SUBJECT = (
    ('Elementary', 'Elementary'),
    ('Junior HS', 'Junior HS'),
    ('Senior HS', 'Senior HS'),
    ('Science Teacher', 'Science Teacher'),
)

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    division = models.CharField(max_length=20, choices=SUBJECT, default='Science Teacher')
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-Profile'