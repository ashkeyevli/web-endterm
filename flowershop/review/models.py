import datetime

from django.db import models

# Create your models here.
from _auth.models import Customer
from _auth.models import Manager


class Comment(models.Model):
    description = models.TextField(verbose_name='Описание', null=True)
    created_date = models.DateField(verbose_name='Дата создания', default= datetime.date.today)

    class Meta:
        abstract = True



class ReviewManager(models.Manager):

    def get_related(self):
        return self.select_related('customer')

    def get_by_customer(self, customer_id):
        return self.get_related().filter(customer=customer_id)

class Review(Comment):
    customer = models.ForeignKey(Customer, verbose_name='Автор', on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    rate = models.PositiveIntegerField('Качество обслуживание', default=0)
    objects = ReviewManager()

class ReplyManager(models.Manager):

    def get_related(self):
        return self.select_related('manager')
#
class Reply(Comment):
    review = models.ForeignKey(Review, verbose_name='Отзыв', on_delete=models.CASCADE, related_name='reply')
    manager = models.ForeignKey(Manager, verbose_name='Автор', on_delete=models.CASCADE, related_name='replies')
