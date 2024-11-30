from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import  basket, Taomlar, mini_card_and_url, UserProduct
# from django.http import HttpResponse
# import numpy as np
from django.contrib import messages
from datetime import datetime

def Umumiy(request):
    hammasi=Taomlar.objects.exclude(mahsulot_turi='milliy')
    urls_mini=mini_card_and_url.objects.all()
    milliy = Taomlar.objects.filter(mahsulot_turi='milliy').all()
    # hammasi2=np.random.choice(hammasi,size=len(hammasi.values()),replace=False)
    product=UserProduct.objects.all().order_by('mahsulot_id')
    # for i in product:
    #     print(i.user_id.id)
    mas=[]
    for i in range(len(hammasi)):
            try:
                h=True
                for j in product:
                    if hammasi[i].id ==j.mahsulot_id.id and request.user.id==j.user_id.id:
                            if j.soni!=0:
                                 mas.append({"id" : hammasi[i].id,
                                  "mahsulot_nomi":  hammasi[i].mahsulot_nomi
                                    ,"mahsulot_izohi": hammasi[i].mahsulot_izohi,
                                     "rasm":hammasi[i].rasm,
                                     "mahsulot_narxi":hammasi[i].mahsulot_narxi*j.soni,
                                     "ulanma_id":j.mahsulot_id.id,
                                     "soni":j.soni
                                     })
                                 h=False
                            else:
                                mas.append({"id": hammasi[i].id,
                                            "mahsulot_nomi": hammasi[i].mahsulot_nomi
                                               ,"mahsulot_izohi": hammasi[i].mahsulot_izohi,
                                            "rasm": hammasi[i].rasm,
                                            "mahsulot_narxi": hammasi[i].mahsulot_narxi,
                                            "ulanma_id": j.mahsulot_id.id,
                                            "soni": j.soni
                                            })
                                h=False
                if h:
                    mas.append({"id": hammasi[i].id,
                                "mahsulot_nomi": hammasi[i].mahsulot_nomi
                                   , "mahsulot_izohi": hammasi[i].mahsulot_izohi,
                                "rasm": hammasi[i].rasm,
                                "mahsulot_narxi": hammasi[i].mahsulot_narxi,
                                "ulanma_id": False,
                                "soni": False
                                })
            except:
                mas.append({"id": hammasi[i].id,
                             "mahsulot_nomi": hammasi[i].mahsulot_nomi
                                , "mahsulot_izohi": hammasi[i].mahsulot_izohi,
                             "rasm": hammasi[i].rasm,
                             "mahsulot_narxi": hammasi[i].mahsulot_narxi,
                             "ulanma_id":False,
                             "soni": False
                             })
    milliy_mat=[]
    for i in range(len(milliy)):
        try:
            h=True
            for j in product:
                if milliy[i].id ==j.mahsulot_id.id and request.user.id==j.user_id.id:
                        if j.soni!=0:
                                milliy_mat.append({"id" : milliy[i].id,
                                "mahsulot_nomi":  milliy[i].mahsulot_nomi
                                ,"mahsulot_izohi": milliy[i].mahsulot_izohi,
                                    "rasm":milliy[i].rasm,
                                    "mahsulot_narxi":milliy[i].mahsulot_narxi*j.soni,
                                    "ulanma_id":j.mahsulot_id.id,
                                    "soni":j.soni
                                    })
                                h=False
                        else:
                            milliy_mat.append({"id": milliy[i].id,
                                        "mahsulot_nomi": milliy[i].mahsulot_nomi
                                            ,"mahsulot_izohi": milliy[i].mahsulot_izohi,
                                        "rasm": milliy[i].rasm,
                                        "mahsulot_narxi": milliy[i].mahsulot_narxi,
                                        "ulanma_id": j.mahsulot_id.id,
                                        "soni": j.soni
                                        })
                            h=False
            if h:
                milliy_mat.append({"id": milliy[i].id,
                            "mahsulot_nomi": milliy[i].mahsulot_nomi
                                , "mahsulot_izohi": milliy[i].mahsulot_izohi,
                            "rasm": milliy[i].rasm,
                            "mahsulot_narxi": milliy[i].mahsulot_narxi,
                            "ulanma_id": False,
                            "soni": False
                            })
        except:
            milliy_mat.append({"id": milliy[i].id,
                            "mahsulot_nomi": milliy[i].mahsulot_nomi
                            , "mahsulot_izohi": milliy[i].mahsulot_izohi,
                            "rasm": milliy[i].rasm,
                            "mahsulot_narxi": milliy[i].mahsulot_narxi,
                            "ulanma_id":False,
                            "soni": False
                            })
    # print(mas,len(hammasi))
    # print(mas)
    # print(mas)
    bazalar={
        'hammasi' : mas,
        'urls_mini' : urls_mini,
        'milliy'  :  milliy_mat,
    }
    return render(request, 'home.html', bazalar)


class TaomDetailViwe(View):
    def get(self,request,a):
        bir = Taomlar.objects.get(id=a)
        umumiy = Taomlar.objects.exclude(id=a)
        # umumiy2=np.random.choice(umumiy,size=len(umumiy.values()),replace=False)
        bazalar = {
            'taomlar': bir,
            'umumiy': umumiy,
        }
        return render(request, 'taom.html', bazalar)
class Milliy_taomDetailViwe(View):
    def get(self,request,a):
        milliy_taom = Taomlar.objects.get(id=a)
        milliy_taomlar = Taomlar.objects.exclude(id=a).filter(mahsulot_turi="milliy")
        # milliy_taomlar2=np.random.choice(milliy_taomlar,size=len(milliy_taomlar.values()),replace=False)
        bazalar = {
            'milliy_taom': milliy_taom,
            'milliy_taomlar': milliy_taomlar,
        }
        return render(request, 'milliy.html', bazalar)
def Fast_Food(request):
    hammasi=Taomlar.objects.filter(mahsulot_turi="fast_food")
    # hammasi2=np.random.choice(hammasi, size=len(hammasi.values()), replace=False)
    bazalar={
        'hammasi':hammasi,
    }
    return render(request, 'fast.html', bazalar)
def Milliy(request):
    hammasi=Taomlar.objects.filter(mahsulot_turi="milliy")
    # hammasi2=np.random.choice(hammasi, size=len(hammasi.values()), replace=False)
    bazalar={
        'hammasi':hammasi,
    }
    return render(request, 'milliy_barcha.html', bazalar)


class Fast_FoodDetailViwe(View):
    def get(self,request,a):
        fast_food = Taomlar.objects.get(id=a)
        fast_foodlar = Taomlar.objects.exclude(id=a).filter(mahsulot_turi="fast_food")
        # fast_foodlar2=np.random.choice(fast_foodlar,size=len(fast_foodlar.values()),replace=False)
        bazalar = {
            'fast_food': fast_food,
            'fast_foodlar': fast_foodlar,
        }
        return render(request, 'fast_food.html', bazalar)
class Payment(LoginRequiredMixin,View):
    def get(self,request,a):
        return redirect('pilus',a)
def Chegirma(request):
        chegirmalar = Taomlar.objects.filter(mahsulot_turi="chegirma")
        # chegirmalar2=np.random.choice(chegirmalar,size=len(chegirmalar.values()),replace=False)
        bazalar = {
            'chegirmalar': chegirmalar,
        }
        return render(request, 'chegirmalar.html', bazalar)
class Chegirma_DetailViwe(View):
    def get(self, request, a):
        chegirma = Taomlar.objects.get(id=a)
        umumiy = Taomlar.objects.exclude(id=a).filter(mahsulot_turi="chegirma")
        # umumiy2=np.random.choice(umumiy,size=len(umumiy.values()),replace=False)
        bazalar = {
            'bir': chegirma,
            'umumiy': umumiy,
        }
        return render(request, 'chegirma.html', bazalar)
class About(TemplateView):
    template_name = 'about.html'

class Qidiruv(View):
    def get(self,request):
        malumot = Taomlar.objects.all()
        if 'q' in request.GET:
            name=request.GET.get('q','')
            malumot = Taomlar.objects.filter(Q(mahsulot_turi__icontains=name) | Q(mahsulot_nomi__icontains=name) | Q(mahsulot_narxi__icontains=name))
        baza = {
            'malumot': malumot,
        }
        return render(request,'search.html',baza)

class Pilus(LoginRequiredMixin,View):
    def get(self,request,a):
        taom = Taomlar.objects.get(id=a)
        product = UserProduct.objects.filter(mahsulot_id=a,user_id=request.user.id)
        soni = 1
        if product:
            product[0].soni +=1
            product[0].save()
            soni = product[0].soni
        else:
            UserProduct.objects.create( 
                mahsulot_id = taom,
                user_id = request.user
            )
        return JsonResponse({'success': True,"product":soni})


class Minus(LoginRequiredMixin,View):
    def get(self,request,a):
        taom = Taomlar.objects.get(id=a)
        product = UserProduct.objects.filter(mahsulot_id=a,user_id=request.user.id)
        soni = 0
        if product:
            if product[0].soni>0:
                product[0].soni -=1
                product[0].save()
            else:
                product[0].soni=0
                product[0].save()
            soni = product[0].soni
        else:
            UserProduct.objects.create(
                mahsulot_id = taom,
                user_id = request.user,
                soni=0
            )
        return JsonResponse({'success': True,"product":soni})
        
class Savat_add(LoginRequiredMixin,View):
    def post(self,request):
            if request.method == 'POST':
                user_id = request.user.id
                mahsulotlar=UserProduct.objects.filter(user_id=request.user.id,soni__gt=0)
                if  mahsulotlar==None:
                    messages.error(request, "Iltimos, mahsulot tanlang.")
                    return redirect('home')
                a=False
                try:
                    t=basket.objects.filter(users_id=user_id)
                    if t:
                        b=t.order_by('malumotlar_list_id')
                        c=[i for i in b]
                        a=c[-1].malumotlar_list_id
                except:
                    pass
                hozirgi_vaqt = datetime.now()
                viloyat = request.POST['viloyat']
                shahar = request.POST['shahar']
                mahalla = request.POST['mahalla']
                uy = request.POST['uy']
                izoh = request.POST['izoh']
                if '' not in [viloyat,shahar,mahalla,uy,izoh]:
                    for taom_id in mahsulotlar:
                        savat = basket.objects.create(
                            taom_id=taom_id.mahsulot_id,
                            users_id=taom_id.user_id,
                            soni=taom_id.soni,
                            joylashuvi_viloyat=viloyat,
                            joylashuvi_shahar=shahar,
                            joylashuvi_mahallasi=mahalla,
                            joylashuvi_uy=uy,
                            joy_izoh=izoh,
                            malumotlar_list_id=a+1,
                            vaqt=hozirgi_vaqt,
                        )
                        savat.save()                 
                    UserProduct.objects.filter(user_id=user_id).delete()
                    messages.success(request, "Mahsulotlar savatga qo'shildi.")
                    return redirect('profile')
                else:
                    messages.error(request, "Iltimos, barcha maydonlarni to'ldiring.")
                    return redirect('zakaz')
            return redirect('home')

class Zakazz(LoginRequiredMixin,View):
    def get(self,request):
        user=UserProduct.objects.filter(user_id=request.user.id,soni__gt=0)
        summa=sum(i.mahsulot_id.mahsulot_narxi*i.soni for i in user)
        # print(summa)
        return render(request, 'payment.html', {"savat":summa})
class Buyurtmalar(LoginRequiredMixin,View):
    def get(self,request):
        users_malumot=basket.objects.filter(users_id=request.user.id).order_by('-malumotlar_list_id')
        # print(users_malumot)
        matritsa=[]
        mas_id=[]
        for i in users_malumot:
            a=[]
            h=None
            joylashuv=None
            for j in users_malumot:
                if i.malumotlar_list_id==j.malumotlar_list_id and (j.id not in mas_id):
                    a.append({
                        'taom_id':j.taom_id,
                        'users_id':j.users_id,
                        'soni':j.soni,
                        'joylashuvi_viloyat':j.joylashuvi_viloyat,
                        'joylashuvi_shahar':j.joylashuvi_shahar,
                        'joylashuvi_mahallasi':j.joylashuvi_mahallasi,
                        'joylashuvi_uy':j.joylashuvi_uy,
                        'joy_izoh':j.joy_izoh,
                        'malumotlar_list_id':j.malumotlar_list_id,
                        'vaqt':j.vaqt
                    })
                    h=j.vaqt
                    
                    joylashuv=f"viloyati :{j.joylashuvi_viloyat}\n shahar :{j.joylashuvi_shahar}\n uy : {j.joylashuvi_uy}\n"
                    mas_id.append(j.id)
            if len(a)>0:
                matritsa.append({'mas':a,
                                 'vaqt':h,
                                'joylashuv':joylashuv,
                                'summa':sum(k['taom_id'].mahsulot_narxi*k['soni'] for k in a)})
        # print(matritsa)
        return render(request,'buyurtmalar.html',{'matritsa':matritsa})
