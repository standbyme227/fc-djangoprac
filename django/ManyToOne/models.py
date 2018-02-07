from django.db import models



# class Car(models.Model):
#     manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
#
# class Menufacturer(models.Model):
#     pass
#
# class Car(models.Model):
#     manufacturer = models.ForeignKey(Menufacturer, on_delete=models.CASCADE)
#
#     # 위의 코드와 아래 Car는 똑같이 동작한다.
#     # 그 중에 위치인자인 Menufacturer를 하나는 ''로 감싼 이유는
#     # 일반적으로 위에서 아래로 순차적으로 해석하는데
#     # 아래쪽의 Car의 Manufacturer은 class Manufacturer가 먼저 선언되고나서,
#     # 선언되고 있기에 그 class명만 적어도 인지하지만
#     # 위쪽의 Car는 Manufacturer보다 먼저 선언되었기에 '문자열'처리를 해야 나중에 선언된 같은 문자열을 참조하여 처리해준다.

class Reporter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASfiCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)