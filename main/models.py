from django.db import models


class User_work:
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Имя')
    login = models.EmailField(max_length=70, verbose_name='Логин')
    passvord = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self) -> str:
        return self.name
    def __str__(self) -> str:
        return self.last_name
    def __str__(self) -> str:
        return self.login
    


class Organizations:
    group = models.CharField(max_length=100, verbose_name='Организация')
    email = models.EmailField(max_length=50, verbose_name='Почта')

    def __str__(self) -> str:
        return self.group
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbouse_name = 'Органицация'
        verbouse_name = 'Организации'
