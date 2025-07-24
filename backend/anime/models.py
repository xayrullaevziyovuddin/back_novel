from django.db import models


class AnimeSeason(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название сезона")
    description = models.TextField(verbose_name="Описание", blank=True)
    release_year = models.IntegerField(verbose_name="Год выпуска")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Сезон аниме"
        verbose_name_plural = "Сезоны аниме"
        ordering = ['-release_year']

    def __str__(self):
        return self.title


class Episode(models.Model):
    season = models.ForeignKey(AnimeSeason, on_delete=models.CASCADE, related_name='episodes', verbose_name="Сезон")
    title = models.CharField(max_length=200, verbose_name="Название серии")
    episode_number = models.PositiveIntegerField(verbose_name="Номер серии")
    video_file = models.FileField(upload_to='videos/', verbose_name="Видео файл", blank=True, null=True)
    description = models.TextField(verbose_name="Описание серии", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"
        ordering = ['episode_number']

    def __str__(self):
        return f"{self.season.title} - Эпизод {self.episode_number}: {self.title}"