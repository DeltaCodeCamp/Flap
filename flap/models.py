from django.db import models

class special(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    phone = models.DecimalField(max_digits = 14, decimal_places = 0)
    signed_up = models.DateTimeField(auto_now_add = True)

class organization(models.Model):
    organization = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    phone = models.DecimalField(max_digits = 14, decimal_places = 0)
    signed_up = models.DateTimeField(auto_now_add = True)
    info = models.CharField(max_length = 500)

class events(models.Model):
    event = models.CharField(max_length = 200)
    location = models.CharField(max_length = 300)
    organization = models.ForeignKey(organization, on_delete = models.CASCADE, blank = True)
    event_on = models.DateTimeField()
    info = models.CharField(max_length = 500)

class special_second(models.Model):
    disabilities_id = models.CharField(max_length = 50)
    interests_id = models.CharField(max_length = 50)
    age = models.DecimalField(max_digits = 3, decimal_places = 1)
    bio = models.CharField(max_length = 500)

class organization_second(models.Model):
    disabilities_id = models.CharField(max_length = 50)
    activities_id = models.CharField(max_length = 50)
    minimum_age = models.DecimalField(max_digits = 3, decimal_places = 1)
    maximum_age = models.DecimalField(max_digits = 3, decimal_places = 1)

class disabilities(models.Model):
    my_choices = (
    ('APD', 'Audiotory Processing Disorder'),
    ('DYC', 'Dyscalculia'),
    ('DYG', 'Dysgraphia'),
    ('DYS', 'Dyslexia'),
    ('LPD', 'Language Processing Disorder'),
    ('NLD','Non Verbal Learning Disabilities'),
    ('VMD', 'Visual Perceptual Motor Deficit'),
    ('ADD', 'Attention Deficient Hyperactivity Disorder'),
    ('DYP', 'Dyspraxia'),
    ('EXF', 'Executive Functioning'),
    ('MEM', 'Memory'),
    )
    disabilities_id = models.CharField(max_length = 50)
    disability = models.CharField(max_length  =3, choices = my_choices)

class interests(models.Model):
    my_choices = (
    ('DNC', 'Dancing'),
    ('SNG', 'Singing'),
    ('SWM', 'Swimming'),
    ('PLN', 'Playing'),
    ('CLC', 'Cycling'),
    ('COG', 'Cognition'),
    )
    interests_id = models.CharField(max_length = 50);
    interests = models.CharField(max_length = 50, choices = my_choices)
