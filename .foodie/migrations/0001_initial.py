# Generated by Django 4.0.2 on 2022-02-22 23:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required Category', max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category safe url')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='foodie.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Not Required', verbose_name='description')),
                ('slug', models.SlugField(max_length=255)),
                ('regular_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 99999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='Regular Price')),
                ('discount_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 99999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='Discount Price')),
                ('is_active', models.BooleanField(default=True, help_text='Change food visibility', verbose_name='food Visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodie.category')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, unique=True, verbose_name='Food type')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Food Type',
                'verbose_name_plural': 'Food Types',
            },
        ),
        migrations.CreateModel(
            name='MeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Meat type')),
                ('price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 99999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='Price')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Meat Type',
                'verbose_name_plural': 'Meat Types',
            },
        ),
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/custom.png', help_text='Upload a food image', upload_to='images/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, help_text='Please add alternative text', max_length=255, null=True, verbose_name='Alternative text')),
                ('is_feature', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_image', to='foodie.food')),
            ],
            options={
                'verbose_name': 'Food Image',
                'verbose_name_plural': 'Food Images',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='foodie.foodtype'),
        ),
        migrations.AddField(
            model_name='food',
            name='meats',
            field=models.ManyToManyField(related_name='meat', to='foodie.MeatType'),
        ),
    ]
