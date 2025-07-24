from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя персонажа")
    alias = models.CharField(max_length=100, verbose_name="Псевдоним", blank=True)
    description = models.TextField(verbose_name="Описание")
    backstory = models.TextField(verbose_name="Предыстория", blank=True)
    image = models.ImageField(upload_to='characters/', verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        ordering = ['name']

    def __str__(self):
        return self.name