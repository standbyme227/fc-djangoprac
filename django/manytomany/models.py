from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    # pulications는 하나의 Article인스턴스에서
    # 해당 인스턴스의 MTM필드에 연결된 Publication목록을 다룰 수 있게 해줍니다.
    # 그러므로 publications는 단하나의 Article 인스턴스의 속성입니다.

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
