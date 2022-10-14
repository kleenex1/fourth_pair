from django.db import models


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    RATING = [  (1, '★'),
                (2, '★★'),
                (3, '★★★'),
                (4, '★★★★'),
                (5, '★★★★★'),]
    grade = models.IntegerField(choices=RATING, default=None)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)

    image1 = models.ImageField(upload_to="review_pics", default=None)
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)

