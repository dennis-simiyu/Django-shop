# Generated by Django 3.1.4 on 2021-10-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0018_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Returned', 'Returned')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='salerdetail',
            name='state',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilfi'), ('Tana_river', 'Tana rive'), ('Lamu', 'Lamu'), ('Taita_taveta', 'Taita taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka_nithi', 'Tharaka nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machaos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Muranga', 'Muranga'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West_Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans_nzoia', 'Trans Nzoia'), ('Uasingishu', 'Uasingishu'), ('Elgeyo_marakwet', 'Elgeyo Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Bungoma', 'Bungoma'), ('Vihiga', 'Vihiga'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homabay', 'Homabay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], max_length=50, null=True),
        ),
    ]
