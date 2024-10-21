# Generated by Django 5.1 on 2024-10-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_alter_promo_code_alter_promo_sale_remove_promo_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersfilter',
            name='filter_name',
            field=models.CharField(help_text='Любое', max_length=200, null=True, verbose_name='Наименование фильтра'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='delivery_variant',
            field=models.CharField(choices=[('s', 'Самовывоз'), ('d', 'Даставка'), ('all', 'Не задано')], default='Не задано', max_length=9, verbose_name='Вариант доставки'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_variant',
            field=models.CharField(choices=[('cash', 'Наличными'), ('card', 'По карте'), ('online', 'Онлайн'), ('all', 'Не задано')], default='Не задано', max_length=9, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='usersfilter',
            name='sex',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский'), ('all', 'Не задано')], default='Не задано', max_length=9, verbose_name='Пол'),
        ),
    ]