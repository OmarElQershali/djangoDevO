from django.db import models
from django.utils import dates
from django.core.validators import MaxValueValidator

class storyModel(models.Model):

    Date = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999)])
    Title = models.CharField(max_length = 50 )
    Depaetment = models.CharField(max_length = 50 )
    Descripion = models.TextField(default='')
    """
    user = models.ForeignKey(User , on_delete = 'None')

    
    img = models.ImageField(upload_to='post_img/' , default=('post_img/default.png'))
    created = models.DateTimeField(default=timezone.now())
    """
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.Depaetment

