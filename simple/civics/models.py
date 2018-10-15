from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.PROTECT)
#     checked_out = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
