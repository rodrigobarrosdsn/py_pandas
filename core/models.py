from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, null=True, blank=False, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    cellphone = models.CharField(max_length=20, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    evaluation = models.FloatField(default=0) #Avaliação

    forgot_password_hash = models.CharField(max_length=255, null=True, blank=True)
    forgot_password_expire = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True) #Data de nascimento
    bith_time = models.TimeField(null=True, blank=True) #Hora de nascimento
    nickname = models.CharField(max_length=255, null=True, blank=True) #Apelido
    date_free_to_travel = models.DateField(null=True, blank=True) #Data livre para viajar
    sons = models.CharField(max_length=255, null=True, blank=True) #Filhos
    participates_social_movement = models.CharField(max_length=255, null=True, blank=True) #Participa de Movimento social
    organ_donor = models.CharField(max_length=255, null=True, blank=True) #Doador de órgãos
    favorite_social_network = models.CharField(max_length=255, null=True, blank=True) #Rede social favorita
    instagram = models.CharField(max_length=255, null=True, blank=True) #Instagram
    twitter = models.CharField(max_length=255, null=True, blank=True) #Twitter
    tiktok = models.CharField(max_length=255, null=True, blank=True) #TikTok
    linkedin = models.CharField(max_length=255, null=True, blank=True) #Linkedin
    facebook = models.CharField(max_length=255, null=True, blank=True) #Facebook
    telegram = models.CharField(max_length=255, null=True, blank=True) #Telegram
    link_name = models.CharField(max_length=255, null=True, blank=True) #Link Name
    favorites = models.CharField(max_length=255, null=True, blank=True) #Favorites Curiosities

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_verified(self):
        return self.is_active

    @property
    def is_staff(self):
        return self.is_admin


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Rule(Base):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    point = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.description} - {self.point}'

class Regra(models.Model):
    rule_name = models.CharField(max_length=100)
    rule_description = models.TextField()
    rule_criteria = models.TextField()
    rule_outcome = models.FloatField(default=0)
    rule_field = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return f'{self.rule_name} - {self.rule_description} - {self.rule_criteria} - {self.rule_outcome}'

class GameData(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    score = models.FloatField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    achievements = models.TextField(blank = True, null = True)