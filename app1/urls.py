from django.urls import path
from .views import (Buyurtmalar, Umumiy,TaomDetailViwe,Milliy_taomDetailViwe,Fast_FoodDetailViwe,
Chegirma_DetailViwe,Payment,Fast_Food,Milliy,Chegirma,About,Qidiruv,Pilus,Minus
,Savat_add,Zakazz
)
urlpatterns=[
    path('', Umumiy, name="home"),
    path('taomlar/<a>/', TaomDetailViwe.as_view(), name="taomlar"),
    path('about/', About.as_view(), name="about"),
    path('fast_food/', Fast_Food, name="fast"),
    path('taomlar/milliy/<a>/', Milliy_taomDetailViwe.as_view(), name="milliy_taom"),
    path('milliy/', Milliy, name="milliy"),
    path('taomlar/fast_food/<a>/', Fast_FoodDetailViwe.as_view(), name="fast_food"),
    path('pul_yuborish/<a>/', Payment.as_view(), name="pul"),
    path('chegirmalar/taomlar/', Chegirma, name="chegirma"),
    path('taomlar/chegirma/<a>/', Chegirma_DetailViwe.as_view(), name="chegirmalar"),
    path('qidiruv/', Qidiruv.as_view(), name="search"),
    path('pilus/<a>/', Pilus.as_view(), name="pilus"),
    path('minus/<a>/',Minus.as_view(),name="minus"),
    path('savat_add/',Savat_add.as_view(),name='savat_add'),
    path('zakaz/',Zakazz.as_view(),name='zakaz'),
    path('buyurtmalar/',Buyurtmalar.as_view(),name='buyurtma'),
]