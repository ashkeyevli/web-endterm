from django.db.models.signals import post_save
from django.dispatch import receiver
from ordering.models import Order, OrderItem
from django.contrib.sessions.backends.db import SessionStore

from product.models import Flower


@receiver(post_save, sender=Order)
def user_created(sender, instance, created, **kwargs):
    if created:
        session = SessionStore(session_key=instance.session_key)
        cart = session.get('cart')
        products = Flower.objects.filter(pk__in=cart.keys())
        for product in products:
            cart[str(product.id)]['flower'] = product

        for item in cart.values():
            order_item = OrderItem.objects.create(order=instance,
                                                  flower=item['flower'],
                                                  quantity=item['quantity'])
        Order.objects.filter(id = instance.id).update(session_key = "")
