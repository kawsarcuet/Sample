from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^List_of_university$', List_of_university, name="List_of_university"),
    url(r'^Rank_of_website$', Rank_of_website, name="Rank_of_website"),
    url(r'^quality_of_website$', quality_of_website, name="quality_of_website"),
    url(r'^Buet$', buet, name="buet"),
    url(r'^Cuet$', cuet, name="cuet"),
    url(r'^Ruet$', ruet, name="ruet"),
    url(r'^Kuet$', kuet, name="kuet"),
    url(r'^Duet$', duet, name="duet"),
    url(r'^Cu$', cu, name="cu"),
    url(r'^Ru$', ru, name="ru"),
    url(r'^Ju$', ju, name="ju"),
    url(r'^Jnu$', jnu, name="jnu"),
    url(r'^Ku$', ku, name="ku"),
    url(r'^Iu$', iu, name="iu"),
    url(r'^Nstu$', nstu, name="nstu"),
    url(r'^Iiuc$', iiuc, name="iiuc"),
    url(r'^Aiub$', aiub, name="aiub"),
    url(r'^Aust$', aust, name="aust"),
    url(r'^Brur$', brur, name="brur"),
    url(r'^Bsmmu$', bsmmu, name="bsmmu"),
    url(r'^Iut$', iut, name="iut"),
    url(r'^Just$', just, name="just"),
    url(r'^Nsu$', nsu, name="nsu"),
    url(r'^Uiu$', uiu, name="uiu"),
    url(r'^Du$', du, name="du"),
    url(r'^Hstu$', hstu, name="hstu"),
    url(r'^Mist$', mist, name="mist"),
    url(r'^Pstu$', pstu, name="pstu"),
    url(r'^Sau$', sau, name="sau"),
    url(r'^Sbau$', sbau, name="sbau"),
    url(r'^Seu$', seu, name="seu"),
    url(r'^Sub$', sub, name="sub"),
    url(r'^Bau$', bau, name="bau"),
    url(r'^Sust$', sust, name="sust"),
    url(r'^Brac$', brac, name="brac"),
    url(r'^Mbtu$', mbtu, name="mbtu"),
    url(r'^Bsmrau$', bsmrau, name="bsmrau"),
    url(r'^Bubt$', bubt, name="bubt"),


]
