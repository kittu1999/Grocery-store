# Generated by Django 3.2 on 2021-05-02 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grocerystore', '0002_remove_grocery_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
