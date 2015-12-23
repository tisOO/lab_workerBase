# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser

from department.models import Department, DepartmentJobPosition
#from honors.models import Salary, Prize, Achievement
from django.utils import timezone

MARITAL_STATUS = (
    ("Single", "Не женат/не замужем"),
    ("In relation ship", "Встречаюсь"),
    ("Engaged", "Помолвлен(а)"),
    ("Married", "Женат/замужем"),
    ("Widower", "Вдова/вдовец"),
    ("In love", "Влюбен(а)"),
    ("It's complicated", "Все сложно"),
    ("Actively searching", "В активном поиске"),
    ("I'm programmer", "Я - программист")

)

USER_TYPES = (
    ("Admin", "Администратор"),
    ("Human resources Department", "Отдел кадров"),
    ("Accounting", "Бухгалтерия"),
    ("Chief", "Начальник"),
    ("Trade union", "Профком"),
    ("Stuff", "Персонал")
)


class Worker(AbstractUser):

    user_type = models.CharField(verbose_name="Тип пользователя", choices=USER_TYPES, max_length=64, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255, null=True)
    sex = models.BooleanField(verbose_name="Пол", default=False)
    birth_place = models.CharField(verbose_name="Место рождения", max_length=255, null=True)
    birthday = models.DateField(verbose_name="Дата рождения", null=True)
    marital_status = models.CharField(verbose_name="Семейное положение", choices=MARITAL_STATUS,
                                      max_length=50, null=True)
    avatar = models.ImageField(verbose_name="Изображение профиля", upload_to='images/web_users/', blank=True, null=True, help_text='User\'s avatar')

    objects = UserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        try:
            job = JobPosition.objects.filter(worker=self).order_by('-id')[0]
        except IndexError:
            job = ""
        return '%s %s %s %s' % (self.last_name, self.first_name, self.patronymic, job)

    def get_avatar_as_html(self):
        return "<img src='/media/%s' height='200px'/>" % self.avatar
    get_avatar_as_html.allow_tags = True
    get_avatar_as_html.short_description = 'Текущее изображение'
    def age(self):
        return int((timezone.now().date() - self.birthday).total_seconds()/31536000.0)
    age.allow_tags = True
    age.short_description = "Возраст"

    def get_sex(self):
        if self.sex:
            return "мужской"
        else:
            return "женский"

    get_sex.allow_tags = True
    get_sex.short_description = "Пол"

    def get_current_job(self):
        try:
            job = JobPosition.objects.filter(worker=self).order_by('-id')[0]
        except IndexError:
            return None
        return job.current_position

    get_current_job.allow_tags = True
    get_current_job.short_description = "Должность"

    def get_current_department(self):
        try:
            job = JobPosition.objects.filter(worker=self).order_by('-id')[0]
        except IndexError:
            return None
        return job.department

    get_current_department.allow_tags = True
    get_current_department.short_description = "Отдел"

    def get_children_count(self):
        return WorkerChild.objects.filter(worker=self).count()

    get_children_count.allow_tags = True
    get_children_count.short_description = "Число детей"

    def get_current_white_salary(self):
        return self.get_current_black_salary()*0.87

    get_current_white_salary.allow_tags = True
    get_current_white_salary.short_description = "Зарплата за этот месяц"


    def get_current_tax(self):
        return self.get_current_black_salary()*0.13

    get_current_tax.allow_tags = True
    get_current_tax.short_description = "Налог за этот месяц"

    def salary_by_month_year(self, month, year):
        from honors.models import Salary
        try:
            salary = Salary.objects.filter(
                worker=self, destination_day__month__lte=month, destination_day__year=year
            ).order_by(
                'id'
            )[0].salary
        except IndexError:
            try:
                salary = Salary.objects.filter(
                    worker=self, destination_day__year__lt=year
                ).order_by(
                    'id'
                )[0].salary
            except IndexError:
                return 0
        return salary

    def salary_by_year(self, year):

        if timezone.now().year == year:
            month = timezone.now().month
        else:
            month = 12

        total_salary = 0
        for i in range(1, month+1):
            salary = self.salary_by_month_year(i, year)
            prize = self.prize_by_month_year(i, year)
            salary += prize
            achievements = self.achievements_profit_by_month_year(i, year)
            if prize - achievements > 0:
                salary += achievements
            salary *= 0.87
            total_salary += salary
        return total_salary

    def salary_by_current_year(self):
        return self.salary_by_year(timezone.now().year)

    salary_by_current_year.allow_tags = True
    salary_by_current_year.short_description = "Доход за текущий год"

    def prize_by_month_year(self, month, year):
        from honors.models import Prize
        try:
            prize = Prize.objects.filter(
                worker=self, destination_day__month__lte=month, destination_day__year=year
            ).order_by(
                'id'
            )[0].prize
        except IndexError:
            try:
                prize = Prize.objects.filter(
                    worker=self, destination_day__year__lt=year
                ).order_by(
                    'id'
                )[0].prize
            except IndexError:
                return 0
        return prize

    def achievements_by_month_year(self, month, year):
        from honors.models import Achievement
        achievements = Achievement.objects.filter(
            worker=self, date__month=month, date__year=year
        )
        return achievements

    def achievements_profit_by_month_year(self, month, year):
        achievements = self.achievements_by_month_year(month, year)
        sum = 0
        for achievement in achievements:
            sum += achievement.allowance
        return sum

    def get_current_black_salary(self):
        from honors.models import Salary
        try:
            salary = Salary.objects.filter(worker=self).order_by('-id')[0].salary
        except IndexError:
            salary = 0
        return salary + self.current_month_prize()

    def current_month_prize(self):
        from honors.models import Prize, Achievement
        try:
            prize = Prize.objects.filter(worker=self).order_by('-id')[0].prize
        except IndexError:
            prize = 0

        date = timezone.now()
        achievements = Achievement.objects.filter(
            worker=self, date__year=date.year, date__month=date.month
        )

        for ach in achievements:
            prize += ach.allowance

        if prize > 0:
            return prize
        return 0

    #
    # def year_salary(self):
    #     pass


class WorkerAdminProxy(Worker):
    class Meta:
        proxy = True
        verbose_name = "Работник (Администратор)"
        verbose_name_plural = 'Работники (Администратор)'


class WorkerHRProxy(Worker):
    class Meta:
        proxy = True
        verbose_name = "Работник (Отдел кадров)"
        verbose_name_plural = 'Работники (Отдел Кадров)'

class WorkerLocation(models.Model):

    worker = models.ForeignKey(Worker)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    house = models.CharField(max_length=32)
    flat = models.PositiveIntegerField()


class WorkerChild(models.Model):

    worker = models.ForeignKey(Worker)
    name = models.CharField(verbose_name="Имя ребенка", max_length=255)
    sex  = models.BooleanField(verbose_name="Пол", default=False)
    birthday = models.DateField(verbose_name="Дата рождения ребенка")

    class Meta:
        verbose_name = "Ребенок работника"
        verbose_name_plural = 'Дети работников'

    def __str__(self):
        return '%s' % self.name

    def age(self):
        return int((timezone.now().date() - self.birthday).total_seconds()/31536000.0)
    age.allow_tags = True
    age.short_description = "Возраст"


class JobPosition(models.Model):

    worker = models.ForeignKey(Worker)
    organization = models.CharField(verbose_name="Название организации", max_length=128, blank=True) # if org is blank, that means current org
    department = models.ForeignKey(Department, null=True, blank=True)
    position = models.CharField(verbose_name="Должность/особое название должности", max_length=128, blank=True)
    current_position = models.ForeignKey(DepartmentJobPosition, verbose_name="Должность на нашем предприятии", blank=True, null=True)
    from_date = models.DateField(verbose_name="Дата начала работы на данной позиции")
    to_date = models.DateField(verbose_name="Дата окончания работы на данной позиции", blank=True, null=True)

    def get_admin_url(self):
        from django.core import urlresolvers
        from django.contrib.contenttypes.models import ContentType
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    def __str__(self):
        if self.position:
            return "%s %s" % (self.position, self.organization)
        return "%s %s" % (self.current_position, self.organization)

    class Meta:
        verbose_name = "Место работы и должность"
        verbose_name_plural = 'Место работы и должность'


class JobPositionReadOnlyProxy(JobPosition):
    class Meta:
        proxy = True
        verbose_name = "Место работы и должность"
        verbose_name_plural = 'Место работы и должность'
