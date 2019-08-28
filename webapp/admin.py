from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
@admin.register(Buet,Cuet,Ruet,Kuet,Duet,Du,Cu,Ru,Ju,Jnu,Ku,Iu,Nstu,Iiuc,Aiub,Aust,Brur,Bsmmu,Iut,Just,Nsu,Uiu,Hstu,Mist,Pstu,Sau,Sbau,Seu,Sub,Sust,Uapb,Iubat,Bsmrau,Dafo,Bau,East,Brac,Mbtu,Iub,Bubt)
class ViewAdmin(ImportExportModelAdmin):
    pass
