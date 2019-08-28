from . models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def List_of_university(request):
    return render(request, 'index1.html')
def quality_of_website(request):
    return render(request, 'quality.html')
def Ran(request,model):
    bu = model.objects.all()
    con=0
    fac=0
    f=0
    for it in bu:
        if(it.contents!="none"):
            con=con+1
        if(it.performance!=0 and it.performance>35):
            perform=it.performance

        if(it.faculty!=105):
            fac=fac+it.faculty
        if(it.loadtime!=0):
            load=10-(it.loadtime/3)
        if(it.notice!=0):
            noti=it.notice
            f=1
        if(f==0):
            noti=0

    if(noti>10):
        noti=10
    fac=fac/5
    if(con>25):
        con=25

    total=((35*con)/25)+(perform/4)+load+((noti*10)/10)+(fac*20)/100
    return total



def Rank_of_website(request):
    dic={}
    total=Ran(request,Buet)
    dic['BUET']=total
    total=Ran(request,Cuet)
    dic['CUET']=total
    total=Ran(request,Kuet)
    dic['KUET']=total
    total=Ran(request,Ruet)
    dic['RUET']=total
    total=Ran(request,Duet)
    dic['DUET']=total
    total=Ran(request,Cu)
    dic['CU']=total
    total=Ran(request,Ru)
    dic['RU']=total
    total=Ran(request,Ju)
    dic['JU']=total
    total=Ran(request,Jnu)
    dic['JNU']=total
    total=Ran(request,Ku)
    dic['KU']=total
    total=Ran(request,Iu)
    dic['IU']=total
    total=Ran(request,Iiuc)
    dic['IIUC']=total
    total=Ran(request,Nstu)
    dic['NSTU']=total
    total=Ran(request,Aiub)
    dic['AIUB']=total
    total=Ran(request,Aust)
    dic['AUST']=total
    total=Ran(request,Brur)
    dic['BRUR']=total
    total=Ran(request,Bsmmu)
    dic['BSMMU']=total
    total=Ran(request,Iut)
    dic['IUT']=total
    total=Ran(request,Just)
    dic['JUST']=total
    total=Ran(request,Nsu)
    dic['NSU']=total
    total=Ran(request,Uiu)
    dic['UIU']=total
    total=Ran(request,Du)
    dic['DU']=total
    total=Ran(request,Hstu)
    dic['HSTU']=total
    total=Ran(request,Mist)
    dic['MIST']=total
    total=Ran(request,Pstu)
    dic['PSTU']=total
    total=Ran(request,Sau)
    dic['SAU']=total
    total=Ran(request,Sbau)
    dic['SBAU']=total
    total=Ran(request,Seu)
    dic['SEU']=total
    total=Ran(request,Sub)
    dic['SUB']=total
    total=Ran(request,Sust)
    dic['SUST']=total

    total=Ran(request,Bsmrau)
    dic['BSMRAU']=total
    total=Ran(request,Bau)
    dic['BAU']=total
    total=Ran(request,Brac)
    dic['BRACU']=total
    total=Ran(request,Mbtu)
    dic['MBTU']=total
    total=Ran(request,Bubt)
    dic['BUBT']=total
    dictt={}
    for word in sorted(dic, key=dic.get, reverse=True):
      dictt[word]=dic[word]

    context = {
        'dictt': dictt,
    }
    return render(request, 'rank.html', context)

def quality(request,model):
    bu = model.objects.all()
    but=model
    con=0
    fac=0
    noti=0
    per=0
    loadt=0
    f=0
    for it in bu:
        if(it.contents!="none"):
            con=con+1
        if(it.performance>35):
            perform=(it.performance)
        if(it.performance!=0 and it.performance<36):
            no=it.performance
        if(it.faculty!=105):
            fac=fac+it.faculty
        if(it.loadtime!=0):
            load=round(10-((it.loadtime)/3),2)
            loadt=it.loadtime
        if(it.notice!=0):
            cnoti=it.notice
            f=1
        if(f==0):
            cnoti=0
    if(cnoti>10):
        noti=10
    else:
        noti=cnoti

    fac=fac/5
    if(con>25):
        con=25
    fcon=(35*con)/25
    fnoti=(noti*10)/10
    ffac=(fac*20)/100
    per=perform/4
    total=fcon+per+load+fnoti+ffac
    ffcon=con*4
    fffac=fac
    ffnoti=noti*10
    total=round(total,2)
    context = {
        'total': total,
        'perform':perform,
        'loadt':loadt,
        'fcon':fcon,
        'fnoti':fnoti,
        'ffac':ffac,
        'ffcon':ffcon,
        'ffnoti':ffnoti,
        'fffac':fffac,
        'bu':bu,
        'con':con,
        'fac':fac,
        'cnoti':cnoti,
        'per':per,
        'load':load,
        'no':no


    }
    return render(request, 'show.html', context)

def buet(request):
    return quality(request,Buet)
def cuet(request):
    return quality(request,Cuet)
def kuet(request):
    return quality(request,Kuet)
def ruet(request):
    return quality(request,Ruet)
def duet(request):
    return quality(request,Duet)
def cu(request):
    return quality(request,Cu)
def ru(request):
    return quality(request,Ru)
def ju(request):
    return quality(request,Ju)
def jnu(request):
    return quality(request,Jnu)
def ku(request):
    return quality(request,Ku)
def iu(request):
    return quality(request,Iu)
def nstu(request):
    return quality(request,Nstu)
def iiuc(request):
    return quality(request,Iiuc)
def aiub(request):
    return quality(request,Aiub)
def aust(request):
    return quality(request,Aust)
def brur(request):
    return quality(request,Brur)
def bsmmu(request):
    return quality(request,Bsmmu)
def iut(request):
    return quality(request,Iut)
def just(request):
    return quality(request,Just)
def nsu(request):
    return quality(request,Nsu)
def uiu(request):
    return quality(request,Uiu)
def du(request):
    return quality(request,Du)
def hstu(request):
    return quality(request,Hstu)
def mist(request):
    return quality(request,Mist)
def pstu(request):
    return quality(request,Pstu)
def sau(request):
    return quality(request,Sau)
def sbau(request):
    return quality(request,Sbau)
def seu(request):
    return quality(request,Seu)
def sub(request):
    return quality(request,Sub)
def sust(request):
    return quality(request,Sust)

def bsmrau(request):
    return quality(request,Bsmrau)
def bau(request):
    return quality(request,Bau)
def brac(request):
    return quality(request,Brac)
def mbtu(request):
    return quality(request,Mbtu)
def bubt(request):
    return quality(request,Bubt)
