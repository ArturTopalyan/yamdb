from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class CreateMixin(GenericViewSet, CreateModelMixin):
    """Mixin обрабатывает запросы на создание объектов."""
    pass


class CategoriesGenresMixin(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin
):
    """Mixin обрабатывает создание, удаление и получение списка объектов."""
    pass
