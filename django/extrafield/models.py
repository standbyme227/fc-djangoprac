from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person, through='Membership')
    # through 옵션이 있는 이유는
    # 중개모델에 foreign key가 2개 있기 때문인가??

    def __str__(self):
        return self.name


        # ExtraField는 ManyToManyField로 묶인 사이에서 생성되는 정보를 저장하는 필드인가???

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # ExtraField엔 ForeignField로 연결되는 class들을 인스턴스에 추가해줘야한다.
    # 두 모델이 관련되는 방식을 정의한다는데 확실히 모르겠다.
    #
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=50)

