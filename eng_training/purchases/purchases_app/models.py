from django.db import models

class Category(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=200)
	class Meta:
	    db_table = 'Categories'


class PurchaseManager(models.Manager):
    def get_from_current_year(self):
        return self.filter(purchased_at__gt='2018-01-01 00:00:00',)


class Purchase(models.Model):
	id = models.BigAutoField(primary_key=True)
	currency = models.CharField(max_length=200)
	country_code = models.CharField(max_length=200)
	category = models.ForeignKey(
        Category,
        db_column='category_id',
        on_delete=models.DO_NOTHING,
        null=True,
    )
	ticket_price_amount = models.BigIntegerField()
	purchased_at = models.DateTimeField()
	quantity_sold = models.IntegerField()
	objects = PurchaseManager()

	class Meta:
		db_table = 'Purchases'

# We need another example as our model does not allow OneToMany relationships
# Let's look at another set of Models to use in this example:
class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)