from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class catagory_of_news(models.Model):

    catagory_name=models.CharField(max_length=300)

    def __str__(self):
        return self.catagory_name

    @staticmethod
    def get_all_category():
        return catagory_of_news.objects.all()



class add_news_new(models.Model):
    name_news=models.CharField(max_length=300)
    catagory=models.ForeignKey(catagory_of_news, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads', default="")
    slug = models.CharField(max_length=130)
    Repoter_name = models.CharField(max_length=300)
    description=models.TextField()
    publish = models.DateTimeField(default=datetime.now(), blank=True)
    likes= models.ManyToManyField(User, related_name='news_post', default=None, blank=True)


    def __str__(self):
        return self.name_news

    @property
    def num_likes(self):
        return self.likes.all().count()


    @staticmethod
    def get_all_product():
        return add_news_new.objects.all()

    @staticmethod
    def get_all_product_by_categoryID(category_id):
        if category_id:
            return add_news_new.objects.filter(catagory=category_id)
        else:
            return add_news_new.get_all_product()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(add_news_new, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self):
        return str(self.post)



class News_Comment(models.Model):
    serial_no = models.AutoField(primary_key=True)
    comment   = models.TextField()
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    post      = models.ForeignKey(add_news_new, on_delete=models.CASCADE)
    postID    = models.CharField(max_length=255)
    parent    = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time_comment = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.comment[0:12] + ".... " + " by " + self.user.username










