from django.db import models
from .categories import Category

class Purchase(models.Model):
	id = models.BigAutoField(primary_key=True)
	currency = models.CharField(max_length=200)
	country_code = models.CharField(max_length=200)
	category = models.ForeignKey(
		Category,
		on_delete=models.DO_NOTHING,
		blank=True, null=True
	)
	ticket_price_amount = models.BigIntegerField()
	purchased_at = models.DateTimeField()
	quantity_sold = models.IntegerField()

	class Meta:
		db_table = 'Purchases'