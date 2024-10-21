# Generated by Django 5.1 on 2024-10-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_usersfilter_filter_name_alter_sale_delivery_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='delivery_variant',
            field=models.CharField(choices=[('s', 'Самовывоз'), ('d', 'Даставка'), ('all', 'Не задано')], default='all', max_length=9, verbose_name='Вариант доставки'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_variant',
            field=models.CharField(choices=[('cash', 'Наличными'), ('card', 'По карте'), ('online', 'Онлайн'), ('all', 'Не задано')], default='all', max_length=9, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='usersfilter',
            name='sex',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский'), ('all', 'Не задано')], default='all', max_length=9, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='usersfilter',
            name='user_id',
            field=models.CharField(help_text='Если скидка не индивидуальная оставьте поле ПУСТЫМ!', max_length=200, null=True, verbose_name='Выбор id пользователя'),
        ),
    ]
