STATUS_NEW = 'new'
STATUS_IN_PROGRESS = 'in_progress'
STATUS_READY = 'ready'
STATUS_COMPLETED = 'completed'

STATUS_CHOICE = (
    (STATUS_NEW, 'Новый заказ'),
    (STATUS_IN_PROGRESS, 'Заказ в обработке'),
    (STATUS_READY, 'Заказ готов к доставке'),
    (STATUS_COMPLETED, 'Заказ выполнен')
)

DELIVERY_TYPE_PICKUP = 'pickup'
DELIVERY_TYPE_COURIER = 'delivery'

DELIVERY_TYPE_CHOICE = (
    (DELIVERY_TYPE_PICKUP, 'Самовывоз'),
    (DELIVERY_TYPE_COURIER, 'Доставка курьером')
)