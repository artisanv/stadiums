from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.



class CustomUserManager(BaseUserManager):

	#private method to becalled from a method ONLY inside the calss
	def _create_user(self,email,password,is_staff,is_superuser, **extra_fileds):
		now =timezone.now()

		if not email :
			raise ValueError('Email must be sent')
			# another way of initializing the object
		email =self.normalize_email(email)


		"""
		the following are inside BaseUserManager or AbstractSuperUser ,,, here are the params for tje default builtin
		user /admin
		"""
		user = self.model(email =email,
						 is_staff =is_staff,
						 is_active =True,
						 is_superuser = is_superuser,
						 last_login = now,
						 date_joined =now,
						 **extra_fileds

			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self,email,password=None,**extra_fileds):
			return self._create_user(email,password,False,False,**extra_fileds)


	def create_superuser(self,email,password,**extra_fileds):
			return self._create_user(email,password,True,True,**extra_fileds)



class CustomUser(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField('email address', max_length=255,unique=True)
	first_name = models.CharField('first name',max_length=255,blank=True,null=True)
	last_name = models.CharField('last name', max_length=255, blank=True,null=True)
	is_staff = models.BooleanField('staff status', default=False)
	is_active = models.BooleanField('active', default=False)
	date_joined = models.DateTimeField('date joined',auto_now_add=True)
    rank = models.FloatField(default=0.0)
	participant = models.ManyToManyField('main.Game')




# the next three fields ... why  ???
	objects = CustomUserManager() # as is

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	#overriding already-there attributes for the meta class to be shows on admin page, but they ar not fields in my defined class, but they are in meta
	#the name user and plural name users will appear properly written as herein admin
	#for ex: city will appear in admin as citys not cities if not set here in meta
	class Meta:
		verbose_name='user'
		verbose_name_plural='users'

		def __unicode__(self):
			return self.first_name

	def get_absolute_url(self):
		return '/users/%s' %(urlquote(self.email))

	def get_full_name(self):
		full_name = '%s %s' %(self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self,subject,message,from_email=None):
		send_mail(subject,message,from_email,[self.email])





class Game(models.Model):

    WEEK_DAYS = (
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNSDAY', 'Wednsday'),
        ('THURSDAY', 'Friday')
    )

    SKILLS = (
		('BEGINNER', 'Beginner'),
		('INTERMEDIATE', 'Intermediate'),
		('ADVANCED', 'Advanced'))

    location = models.CharField('location', max_length=255, blank=True, null=True)
    day  = models.CharField(max_length=100, choices= WEEK_DAYS, default='SUNDAY')
    time  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    title = models.CharField('title',max_length=255,blank=True,null=True)
    skill  = models.CharField(max_length=100, choices= SKILLS, default='BEGINNER')
    custom_user = models.ForeignKey('main.CustomUser')
    finished = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Game_result(models.Model):
    title = models.CharField(max_length=255)
    result = models.SlugField()
    winner = models.CharField('winner',max_length=255)
    winner_image = models.ImageField()
    loser = models.CharField('winner',max_length=255)
    loser_image = models.ImageField()

    def __unicode__(self):
        return self.title
