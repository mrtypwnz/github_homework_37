from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=80, verbose_name='Задача')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, blank=True, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    due_date = models.DateTimeField(verbose_name='Выполнить к')

    def __str__(self):
        return f"{self.pk}. {self.name} ({self.status})"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
