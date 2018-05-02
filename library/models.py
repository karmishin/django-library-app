from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % (self.name)


class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=25)
    pub_date = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title)