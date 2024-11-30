from django.contrib import admin
# Register your models here.
from .models import basket, Taomlar,mini_card_and_url,UserProduct

admin.site.register(Taomlar)
admin.site.register(mini_card_and_url)
admin.site.register(UserProduct)
admin.site.register(basket)
# admin.site.register(Zakazlar)