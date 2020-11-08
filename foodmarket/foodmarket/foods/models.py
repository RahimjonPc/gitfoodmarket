from django.db import models
from django.contrib.auth.models import User
from foodslogic.models import Foods

# class Foods(models.Model):
    # author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Owner', blank = True,null = True)
    # name = models.CharField(max_length = 50)
    # description = models.TextField()
    # poster = models.ImageField(upload_to='posters')
    # price = models.IntegerField()

    # def __str__(self):
        # return self.name

    # class Meta:
        # verbose_name_plural = 'Foods'


class Comments(models.Model):
    food = models.ForeignKey(Foods, on_delete = models.CASCADE, verbose_name = 'Food', blank = True,null = True, related_name = 'comments_food')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Author comment', blank = True,null = True)
    create_date = models.DateTimeField(auto_now = True)
    text = models.TextField(verbose_name = 'Text comment')
    status = models.BooleanField(verbose_name = 'Status comment', default = False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Comments'


