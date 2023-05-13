from django.db.models.signals import post_save, pre_save
from .models import Cart, CartProcessOrders


def post_save_create_cart_process_orders(sender,  instance, created, **kwargs) :
    if created :
        obj = CartProcessOrders.objects.create(
            product             = instance.product,
            order               = instance.order,
            color               = instance.color,
            size_number         = instance.size_number,
            size                = instance.size,
            quantity            = instance.quantity,
            total_price         = instance.total_price,
            id_cart             = instance.id,
            id_nub_product      = instance.product.id,
            transection_id      = instance.transection_id
        )
post_save.connect(post_save_create_cart_process_orders, sender=Cart)


def pre_save_change_product_status(sender, instance, **kwargs) :
    try :
        obj = CartProcessOrders.objects.filter()
    except :
        obj = None
    if obj :
        for item in obj :
            if item.id_nub_product == instance.product.id and item.order == instance.order:
                item.quantity = instance.quantity
                item.save()
                
pre_save.connect(pre_save_change_product_status, sender=Cart)