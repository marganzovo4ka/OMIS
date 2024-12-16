from django.db import models

class User(models.Model):
    name = models.TextField()
    mail = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.mail

class Excursion(models.Model):
    popularity = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Catalog(models.Model):
    excursions = models.ManyToManyField(Excursion, related_name="каталоги")

class Personal_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="личный_кабинет")
    featured_excursions = models.ManyToManyField(Excursion, related_name="в_избранном", blank=True)
    my_excursions = models.ManyToManyField(Excursion, related_name="мои", blank=True)

class Recommendations(models.Model):
    popular_excursions = models.ManyToManyField(Excursion, related_name="рекомендации")