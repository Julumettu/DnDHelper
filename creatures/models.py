from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    allignment = models.CharField(max_length=30)
    armor_class = models.IntegerField()
    hit_points = models.IntegerField()
    hit_points_dice = models.CharField(max_length=10)
    speed = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma= models.IntegerField()
    skills = models.CharField(max_length=600)
    abilities = models.CharField(max_length=600)
    actions = models.CharField(max_length=600)

    def __str__(self):
        return str(self.name)

