from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Food Category Table implimented with Modified Preorder Tree Traversal(mptt)
    """
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_('Required Category'),
        max_length=255,
        unique=True
    )
    slug = models.SlugField(verbose_name=_(
        'Category safe url'), max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse('foodie:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class FoodType(models.Model):
    """
    FoodType Table give a list of the different types of of food available
    """
    name = models.CharField(verbose_name=_('Food type'),
                            help_text=_('Required'), max_length=255)
    # slug = models.SlugField(verbose_name=_(
    # 'Food Type url'), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Food Type')
        verbose_name_plural = _('Food Types')

    def __str__(self):
        return self.name


class Food(models.Model):
    '''
    Food Table containing all food items
    '''
    meats = models.ManyToManyField(
        'MeatType', related_name=_('meat'))
    food_type = models.ForeignKey(
        FoodType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(verbose_name=_(
        'title'), help_text=_('Required'), max_length=255)
    description = models.TextField(verbose_name=_(
        'description'), help_text=_('Not Required'), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(verbose_name=_('Regular Price'), help_text=_(
        'Maximum 99999.99'), error_messages={"name": {"max_length": _('The price must be between 0 and 99999.99.')}}, max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(verbose_name=_('Discount Price'), help_text=_(
        'Maximum 99999.99'), error_messages={"name": {"max_length": _('The price must be between 0 and 99999.99.')}}, max_digits=7, decimal_places=2)
    is_active = models.BooleanField(verbose_name=_(
        'food Visibility'), help_text=_('Change food visibility'), default=True)

    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Food")
        verbose_name_plural = _('Foods')

    def get_absolute_url(self):
        return reverse("foodie:food_detail", args=[self.slug])

    def __str__(self):
        return self.title


class FoodImage(models.Model):
    '''
    The food image table
    '''
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name='food_image')
    image = models.ImageField(verbose_name=_('image'), help_text=_(
        'Upload a food image'), upload_to='images/', default='images/custom.png')
    alt_text = models.CharField(verbose_name=_('Alternative text'),
                                help_text=_('Please add alternative text'), max_length=255, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Food Image')
        verbose_name_plural = _('Food Images')


class MeatType(models.Model):
    '''
    The type of meat on the ordered food
    '''
    # food = models.ForeignKey(
    #    Food, on_delete=models.CASCADE, related_name='meat')
    name = models.CharField(verbose_name=_('Meat type'),
                            help_text=_('Required'), max_length=255)
    price = models.DecimalField(verbose_name=_('Price'), help_text=_(
        'Maximum 99999.99'), error_messages={"name": {"max_length": _('The price must be between 0 and 99999.99.')}}, max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Meat Type')
        verbose_name_plural = _('Meat Types')

    def __str__(self):
        return self.name
