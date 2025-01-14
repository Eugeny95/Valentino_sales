# Generated by Django 5.1 on 2024-10-17 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salevolume',
            name='gift_iico_id',
        ),
        migrations.AddField(
            model_name='sale',
            name='sale',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.salevolume'),
        ),
        migrations.AddField(
            model_name='salevolume',
            name='gift_position',
            field=models.ManyToManyField(to='sale.position'),
        ),
        migrations.AddField(
            model_name='useriico',
            name='iico_id',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='delivery_variant',
            field=models.CharField(choices=[('s', 'Самовывоз'), ('d', 'Даставка'), ('all', 'Не задано')], max_length=9),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_variant',
            field=models.CharField(choices=[('cash', 'Наличными'), ('card', 'По карте'), ('online', 'Онлайн'), ('all', 'Не задано')], max_length=9),
        ),
        migrations.AlterField(
            model_name='salevolume',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='salevolume',
            name='type_of_sale',
            field=models.CharField(choices=[('F', 'Фиксированаая'), ('P', 'В процентах'), ('G', 'Подарок')], max_length=1),
        ),
        migrations.AlterField(
            model_name='useriico',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usersfilter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usersfilter',
            name='sex',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский'), ('all', 'Не задано')], max_length=9),
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('sale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sale.sale')),
                ('users', models.ManyToManyField(to='sale.useriico')),
            ],
        ),
    ]
