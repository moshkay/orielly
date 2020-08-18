from django.db import models

#https://learning.oreilly.com/api/v2/search/?query=python&fields=description&fields=publishers


class AbstractModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Book(AbstractModel):
    title = models.CharField(max_length=200, )
    isbn = models.CharField(max_length=50, null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'









