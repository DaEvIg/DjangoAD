from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from safedelete import SOFT_DELETE, SOFT_DELETE_CASCADE, DELETED_INVISIBLE, DELETED_VISIBLE_BY_PK
from safedelete.models import SafeDeleteModel
from safedelete.managers import SafeDeleteManager


class AdManager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class Ad(SafeDeleteModel):
    deleted_by_cascade = True
    _safedelete_policy = SOFT_DELETE_CASCADE
    CHOICE_CATEGORY = (('Недвижимость', 'Недвижимость'),
                       ('Транспорт', 'Транспорт'),
                       ('Работа', 'Работа'),
                       ('Услуги', 'Услуги'),
                       ('Вещи', 'Вещи'),
                       ('Бизнес', 'Бизнес')
                      )
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CHOICE_CATEGORY, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    objects = AdManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

