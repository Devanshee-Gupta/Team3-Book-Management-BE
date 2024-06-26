# Generated by Django 5.0.1 on 2024-02-05 13:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=30)),
                ('Genre', models.CharField(max_length=20)),
                ('Price', models.FloatField()),
                ('PublishYear', models.CharField(max_length=4)),
                ('Image', models.URLField(max_length=128)),
                ('Description', models.TextField(max_length=700)),
                ('AvailQuantity', models.IntegerField()),
                ('SoldQuantity', models.IntegerField()),
                ('Language', models.CharField(max_length=20)),
                ('OverallRating', models.FloatField(max_length=100)),
                ('TotalReviews', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('CartId', models.AutoField(primary_key=True, serialize=False)),
                ('TotalQuantity', models.IntegerField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('PlacedTime', models.DateTimeField(auto_now_add=True)),
                ('TotalQuantity', models.IntegerField()),
                ('TotalAmount', models.FloatField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('SellerId', models.AutoField(primary_key=True, serialize=False)),
                ('Company', models.TextField(max_length=32)),
                ('CompanyLocation', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=32)),
                ('LastName', models.CharField(max_length=32)),
                ('Email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')])),
                ('Password', models.CharField(max_length=4096, validators=[django.core.validators.RegexValidator(code='invalid_password_format', message='Password must contain at least one lowercase letter, one uppercase letter, and be at least 5 characters long.', regex='^(?=.*[a-z])(?=.*[A-Z]).{5,}$')])),
                ('PhoneNo', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Phone number must be exactly 10 digits.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Phone number must be exactly 10 digits.'), django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be a 10-digit integer.', regex='^\\d{10}$')])),
                ('Address', models.CharField(max_length=100)),
                ('Role', models.CharField(choices=[('Buyer', 'Buyer'), ('Seller', 'Seller'), ('Admin', 'Admin')], default='Buyer', max_length=6)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='CartElement',
            fields=[
                ('CartElementId', models.AutoField(primary_key=True, serialize=False)),
                ('ElementQuantity', models.IntegerField()),
                ('BookObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('CartObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cart')),
            ],
            options={
                'db_table': 'cartelement',
            },
        ),
        migrations.CreateModel(
            name='OrderElement',
            fields=[
                ('OrderElementId', models.AutoField(primary_key=True, serialize=False)),
                ('ElementQuantity', models.IntegerField()),
                ('ElementTotalPrice', models.FloatField()),
                ('BookObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('OrderObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
            options={
                'db_table': 'orderelement',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('RequestId', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default='Pending', max_length=8)),
                ('SellerObj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.seller')),
            ],
            options={
                'db_table': 'request',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='SellerObj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.seller'),
        ),
        migrations.AddField(
            model_name='seller',
            name='UserObj',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('ReviewId', models.AutoField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField()),
                ('ReviewComment', models.TextField(max_length=128)),
                ('ReviewDate', models.DateTimeField(auto_now_add=True)),
                ('BookObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('UserObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='UserObj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.AddField(
            model_name='cart',
            name='UserObj',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('ListId', models.AutoField(primary_key=True, serialize=False)),
                ('TotalQuantity', models.IntegerField()),
                ('UserObj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
            options={
                'db_table': 'wishlist',
            },
        ),
        migrations.CreateModel(
            name='WishListElement',
            fields=[
                ('ListElementId', models.AutoField(primary_key=True, serialize=False)),
                ('BookObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('ListObj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wishlist')),
            ],
            options={
                'db_table': 'wishlistelement',
            },
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('SellerObj', 'Title')},
        ),
    ]
