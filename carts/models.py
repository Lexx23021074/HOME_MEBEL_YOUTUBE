from django.db import models
from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Користувач'
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошики'

    objects = CartQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
                    user_info = self.user.username
        else:
            # Для анонімних кошиків використовуємо ключ сесії або просто "Анонім"
            user_info = f"Анонім (Session: {self.session_key})" if self.session_key else "Анонім"
        
        return f'Кошик {user_info} | Товар {self.product.name} | Кількість {self.quantity}'



