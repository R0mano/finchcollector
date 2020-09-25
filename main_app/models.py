from django.db import models
from django.urls import reverse

FORCE = (
  ('N', "Doesn't have the force"),
  ('B', 'Bright side'),
  ('D', 'Dark side')
)

# Create your models here.

class Spaceship(models.Model):
  name = models.CharField(max_length=100)
  spaceship_type = models.CharField(max_length=100, default='')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("spaceships_detail", kwargs={"pk": self.id})
  

class Character(models.Model):
  name = models.CharField(max_length=100)
  origin = models.CharField(max_length=100)
  light_saber_color = models.CharField(max_length=10)
  has_force = models.BooleanField(default=False)
  spaceships = models.ManyToManyField(Spaceship)

  def __str__(self):
    return f"{self.name} from {self.origin}"

  def get_absolute_url(self):
      return reverse("detail", kwargs={"character_id": self.id})
  
class Force(models.Model):
  force_side = models.CharField(
    max_length=1,
    choices=FORCE,
    default=FORCE[0][0]
    )
  
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"On the {self.get_force_side_display()} side of the Force." 

  
