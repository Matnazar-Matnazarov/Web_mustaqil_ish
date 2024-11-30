from django.db import models
from users.models import CustomUser
from django.urls import reverse

class Taomlar(models.Model):
    mahsulot_nomi = models.CharField(max_length=100)
    mahsulot_izohi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='fayl/', blank=True, null=True)
    mahsulot_narxi = models.IntegerField(blank=True, null=True)
    mahsulot_turi = models.CharField(max_length=100)

    def __str__(self):
        return f"id: {self.id}  {self.mahsulot_nomi}"

class mini_card_and_url(models.Model):
    urls_nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='mini_card/', blank=True, null=True)

    def __str__(self):
        return self.urls_nomi

class UserProduct(models.Model):
    mahsulot_id = models.ForeignKey(Taomlar, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    soni = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"id: {self.id}  username : {self.user_id}  mahsulot_nomi: {self.mahsulot_id.mahsulot_nomi}"

class basket(models.Model):
    taom_id = models.ForeignKey(Taomlar, on_delete=models.CASCADE, null=True)
    users_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True) 
    soni = models.IntegerField(default=0)
    joylashuvi_viloyat = models.CharField(max_length=500)
    joylashuvi_shahar = models.CharField(max_length=500)
    joylashuvi_mahallasi = models.CharField(max_length=200)
    joylashuvi_uy = models.CharField(max_length=200)
    joy_izoh = models.CharField(max_length=200)
    malumotlar_list_id = models.IntegerField()
    vaqt = models.DateTimeField()

    def __str__(self) -> str:
        return f"id: {self.id}  username: {self.users_id.username}   zakaz_id :{self.malumotlar_list_id}"