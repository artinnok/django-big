from django.db import models


class Titleable(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )

    class Meta:
        abstract = True


class Textable(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )

    class Meta:
        abstract = True


class Descriptionable(models.Model):
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        abstract = True


class ShortDescriptionable(models.Model):
    short_description = models.TextField(
        verbose_name='Краткое описание',
        max_length=500
    )

    class Meta:
        abstract = True


class Imageable(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
    )

    class Meta:
        abstract = True


class Emailable(models.Model):
    email = models.EmailField(
        verbose_name='Электронная почта'
    )

    class Meta:
        abstract = True


class Phoneable(models.Model):
    phone = models.CharField(
        verbose_name='Контактный телефон',
        max_length=50
    )

    class Meta:
        abstract = True
