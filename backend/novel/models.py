from django.db import models


class Volume(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название тома")
    description = models.TextField(verbose_name="Описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Том"
        verbose_name_plural = "Тома"
        ordering = ['id']

    def __str__(self):
        return self.title


class Chapter(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name='chapters', verbose_name="Том")
    title = models.CharField(max_length=200, verbose_name="Название главы")
    audio_file = models.FileField(upload_to='audio/', verbose_name="Аудиофайл", blank=True, null=True)
    illustration = models.ImageField(upload_to='illustrations/', verbose_name="Иллюстрация", blank=True, null=True)
    content = models.TextField(verbose_name="Текст главы", blank=True)
    order = models.PositiveIntegerField(verbose_name="Порядок", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"
        ordering = ['order']

    def __str__(self):
        return f"{self.volume.title} - {self.title}"