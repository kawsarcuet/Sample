from django.db import models

class table(models.Model):

    contents = models.CharField(max_length=400,default='none')
    faculty=models.IntegerField(default=105)
    notice=models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    loadtime=models.FloatField(default=0)



    class Meta:
        abstract = True

    def __str__(self):
        return 'contents: {0} faculty: {1} notice: {2} '.format(self.contents, self.faculty, self.notice)

class Buet(table):
    pass

class Cuet(table):
    pass

class Ruet(table):
    pass
class Kuet(table):
    pass

class Duet(table):
    pass

class Du(table):
    pass
class Cu(table):
    pass

class Ru(table):
    pass

class Ju(table):
    pass
class Jnu(table):
    pass

class Ku(table):
    pass

class Iu(table):
    pass
class Nstu(table):
    pass

class Iiuc(table):
    pass
class Aiub(table):
    pass

class Aust(table):
    pass

class Brur(table):
    pass
class Bsmmu(table):
    pass

class Iut(table):
    pass

class Just(table):
    pass
class Nsu(table):
    pass

class Uiu(table):
    pass
class Hstu(table):
    pass
class Mist(table):
    pass

class Pstu(table):
    pass

class Sau(table):
    pass
class Sbau(table):
    pass

class Seu(table):
    pass

class Sub(table):
    pass
class Sust(table):
    pass

class Uapb(table):
    pass
class Iubat(table):
    pass
class Bsmrau(table):
    pass

class Dafo(table):
    pass

class Bau(table):
    pass
class East(table):
    pass

class Brac(table):
    pass

class Mbtu(table):
    pass
class Iub(table):
    pass

class Bubt(table):
    pass
