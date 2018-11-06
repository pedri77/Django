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

    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.get_status_display())
