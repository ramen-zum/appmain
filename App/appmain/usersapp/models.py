from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Описание модели данных. Схема базы данных.
# ========= Administrators data =======================
# Локация (для месторасположения заведения)
class Location(models.Model):
    countryName = models.CharField(max_length=50, default="KZ")
    locationName = models.CharField(max_length=50)
    code = models.CharField(max_length=8, unique=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.locationName


# Вид деятельности заведения
class Type_of_activity(models.Model):
    categoryCode = models.CharField(max_length=50)
    categoryName = models.CharField(max_length=50)
    activityName = models.CharField(max_length=50)
    codeOfActivity = models.CharField(max_length=50, unique=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activityName
# ====================================


# ========== Partners data ===========================
# Рестораны, заведения
class Company (models.Model):
    memberName = models.CharField(max_length=50, db_index=True)
    companyCode = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)
    contacts = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    idOfActivity = models.ForeignKey(Type_of_activity, on_delete=models.CASCADE)
    idOFLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    workingShedule = models.CharField(max_length=50)
    isActive = models.BooleanField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, null = True, blank = True)
#  partner_id = models.ForeignKey(User, on_delete=models.CASCADE) # для отображения компании доступность только партнеру

# для генерации ссылок на конкретное заведение
    def get_absolute_url(self):
        return reverse('object_detail_url', kwargs={'slug': self.slug} )

    def __str__(self):
        return self.memberName


# Меню (только для заведения общепита)
class Menu(models.Model):
    menuName = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=1000)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_datetime = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField()

    def __str__(self):
        return self.menuName
        

# Столы заведений
class Table_of_restaurant(models.Model):
    table_number = models.CharField(max_length=50)
    table_desc = models.CharField(max_length=1000)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField()

    def __str__(self):
        return self.table_number

# Услуги заведений
class Services_of_institutions(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.CharField(max_length=1000)
    service_price = models.DecimalField(decimal_places=2, max_digits=10)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    service_duration = models.DurationField(max_length=1000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField()

    def __str__(self):
        return self.service_name
# ====================================


# ========== Customers data ===========================
# Заказы
class Order(models.Model):
    orderCode = models.CharField(max_length=50)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    isPrepayment = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table_of_restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderCode

# Обзоры и рейтинг заведения и столов (если общепит)
class Review(models.Model):
    Rating = ((1, 'Bad'),
               (2, 'Not Bad'),
               (3, 'Medium'),
               (4, 'Good'),
               (5, 'Great'))
    orderDate = models.DateField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    commentOfReview = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1, choices=Rating)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentOfReview
# ===========================================
