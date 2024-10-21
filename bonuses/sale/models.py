from typing import List
from django.db import models

# Create your models here.

class UserIICO(models.Model):
    iico_id = models.CharField(max_length=120, default='')
    name = models.CharField(max_length=200)
    TYPES_OF_SEX = (
        ('m', 'Мужской'),
        ('f', 'Женский'),
        ('all', 'Не задано'),
        
    )
    sex = models.CharField(choices=TYPES_OF_SEX, default='all', max_length=9, null=True, verbose_name='Пол')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)
'''
Пользовтельстъкий фильтр Пользователь:
- user_id: -1 если скидка не индивидуальна
- мужчина/женщина: выбор Male, Female, FM
- стартовый возраст: 0
- конечный возраст: 100
'''
# условия
'''
Деление на услуги и товары. скидка на то или на то. 
Доставка это товар. 
Оплата картой это товар.

самовывоз/доставка
наличные/карта
скидка на период
скидка в день рождения
ежедневная скидка (по времени) (на услуги или товары)
промокод

'''


# TODO: Промокоды


class Position(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=300)
    cost = models.FloatField()


class SaleVolume(models.Model):
    def __str__(self):
        return str(self.title)
    title = models.CharField(max_length=300, null=True, verbose_name='Название')
    TYPES = (
        ('F', 'Фиксированаая'),
        ('P', 'В процентах'),
        ('G', 'Подарок'),
        
    )
    type_of_sale = models.CharField(choices=TYPES, max_length=1, verbose_name='Вид скидки')
    value_of_sale = models.FloatField(verbose_name='Значение')
    gift_position= models.ManyToManyField(Position, blank=True, null=True, verbose_name='Блюдо в подарок', help_text='Заполнять только если выбран вид скидки - "Подарок"')


class UsersFilter(models.Model):
    filter_name = models.CharField(max_length=200, null=True, verbose_name='Наименование фильтра', help_text='Любое')
    user_id = models.CharField(max_length=200, default='all', null=True, verbose_name='Выбор id пользователя', help_text='Если скидка не индивидуальная НЕ меняйте значение поля!')
    start_age = models.IntegerField(verbose_name='Начальный возраст', default=0)
    end_age = models.IntegerField(verbose_name='Максимальный возраст', default=150)
    TYPES_OF_SEX = (
        ('m', 'Мужской'),
        ('f', 'Женский'),
        ('all', 'Не задано'),
        
    )
    sex = models.CharField(choices=TYPES_OF_SEX, default='all', max_length=9, verbose_name='Пол')
    def __str__(self):
        return str(self.filter_name)




class Sale(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    descryption = models.TextField(verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Изображение')
    start_date = models.DateField(verbose_name='Дата начала акции')
    end_date = models.DateField(verbose_name='Дата окончания акции')
    in_day_start_time = models.TimeField(verbose_name='Время начала акции', help_text='Акция действует в течении выбранного периода времени ежедневно. Следует указать временные рамки действия акции в течение дня')
    in_day_end_time = models.TimeField(verbose_name='Время окончания акции')
    start_cost = models.FloatField(verbose_name='Начальная стоимость', default=0, help_text='Акция действует, если стоимость заказа больше указанной')
    end_cost = models.FloatField(verbose_name='Конечная стоимость', default=1000000000000, help_text='Акция действует, если стоимость заказа меньше указанной')
    DELIVERY_TYPES = (
        ('s', 'Самовывоз'),
        ('d', 'Даставка'),
        ('all','Не задано'),       
    )
    
    delivery_variant = models.CharField(choices=DELIVERY_TYPES, max_length=9, default='all', verbose_name='Вариант доставки')
    
    PAYMENT_TYPES = (
        ('cash','Наличными'),
        ('card', 'По карте'),
        ('online','Онлайн'),
        ('all', 'Не задано'),       
    )

    payment_variant = models.CharField(choices=PAYMENT_TYPES, default='all', max_length=9, verbose_name='Способ оплаты')
    sale = models.OneToOneField(SaleVolume, on_delete=models.CASCADE, null=True, verbose_name='Тип скидки')
    users_filter = models.OneToOneField(UsersFilter, on_delete=models.CASCADE, verbose_name='Пользовательский фильтр', help_text='Выбор группы пользователей по поло-возрастному признаку, либо конкретного пользователя')
    positions = models.ManyToManyField(Position, verbose_name='Позиции меню', help_text='Выбор позиций, на которые распространяется акция') 
    def __str__(self):
        return str(self.title)

class Promo(models.Model):
    code = models.CharField(max_length=10, verbose_name='Промокод')
    user = models.ManyToManyField(UserIICO, default=None, verbose_name='Пользователи')
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE, verbose_name='Тип скидки')