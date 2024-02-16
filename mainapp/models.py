from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last name')
    avatar = models.ImageField(upload_to='students/', verbose_name='avatar', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural= ' студентики'
        ordering = ('last_name',)
