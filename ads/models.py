from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):

    PUBLISHED = 'PUB'
    RESERVED = 'RES'
    SOLD = 'SLD'

    STATUS = (
        (PUBLISHED, 'Published'),
        (RESERVED, 'Reserved'),
        (SOLD, 'Sold')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.get_status_display())
