from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.


class EUser(User):
    phone_number_validator = RegexValidator(
        regex=r'^(\+?234|0)(81|80|70|90|91)\d{8}$',
        message='Phone Number must be entered in the correct format')
    account_number_validator = RegexValidator(
        regex=r'^\d{10}$',
        message='Enter a valid account Number')
    phone_number = models.CharField(
        validators=[phone_number_validator], max_length=14, blank=True)
    account_number = models.CharField(
        validators=[account_number_validator], max_length=10, blank=True)
    address = models.TextField(blank=True)
    address_state = models.CharField(max_length=100, default='Osun')
    address_poster_code = models.IntegerField(default=22222)

    class Meta:
        abstract = True


class Customer(EUser):
    #foods = models.ManyToManyField('Food')

    def __str__(self):
        return self.username


class UserLogin(models.Model):
    password_hash = models.CharField(max_length=32)
    locked_out = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{'on' if self.locked_out else 'off'}__{self.password_hash})"


class CustomerLogin(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class VendorLogin(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    regular_price = models.DecimalField(
        help_text='Maximum 99999.99',
        error_messages={
            "name": {"max_length": 'The price must be between 0 and 99999.99.'}},
        max_digits=7, decimal_places=2
    )
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Food(Product):
    discount_price = models.DecimalField(
        help_text='Maximum 99999.99',
        error_messages={
            "name": {"max_length": 'The price must be between 0 and 99999.99.'}},
        max_digits=7, decimal_places=2
    )
    category = models.ManyToManyField('Category')
    meats = models.ManyToManyField('Meat', blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name', 'vendor'], name='unique product_name_and_vendor')]


class Meat(Product):
    amount_available = models.IntegerField()


class Vendor(EUser):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Image(models.Model):
    is_feature = models.BooleanField(default=False)
    alt_text = models.CharField(max_length=100, blank=True)
    image_height = models.CharField(max_length=4, blank=True, editable=False)
    image_width = models.CharField(max_length=4, blank=True, editable=False)

    class Meta:
        abstract = True


class FoodImage(Image):
    food_images = models.ImageField(upload_to='products/foods/%Y_%m_%d/',
                                    height_field='image_height', width_field='image_width')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)


class MeatImage(Image):
    meat_images = models.ImageField(upload_to='products/meats/%Y_%m_%d/',
                                    height_field='image_height', width_field='image_width')
    meat = models.ForeignKey(Meat, on_delete=models.CASCADE, null=True)


class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(
        help_text='Maximum 99999.99',
        error_messages={
            "name": {"max_length": 'The price must be between 0 and 99999.99.'}},
        max_digits=7, decimal_places=2
    )


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)
    quantity = models.IntegerField()
    price = models.DecimalField(
        help_text='Maximum 99999.99',
        error_messages={
            "name": {"max_length": 'The price must be between 0 and 99999.99.'}},
        max_digits=7, decimal_places=2
    )


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status_code = models.ForeignKey(
        'OrderStatusCode', on_delete=models.CASCADE)
    customer_comments = models.TextField(blank=True)


class OrderStatusCode(models.Model):
    status_code = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status_code


class Shipment(models.Model):
    order = models.ManyToManyField(Order)
    to_address = models.TextField(blank=True)
    from_address = models.TextField(blank=True)
    tracking_no_validator = RegexValidator(regex=r'^\d{20}')
    tracking_no = models.CharField(
        validators=[tracking_no_validator], max_length=20)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_no}_{self.sent_at}"


class ShipmentItem(models.Model):
    shipment_id = models.OneToOneField(Shipment, on_delete=models.CASCADE)
    order_item_id = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
