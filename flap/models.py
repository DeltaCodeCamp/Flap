from django.db import models
disability_choices = (
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
activities_choices = (
('DNC', 'Dancing'),
('SNG', 'Singing'),
('SWM', 'Swimming'),
('PLN', 'Playing'),
('CLC', 'Cycling'),
('COG', 'Cognition'),
)

class special(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    phone = models.DecimalField(max_digits = 14, decimal_places = 0)
    signed_up = models.DateTimeField(auto_now_add = True)
    activated = models.BooleanField(default = False)

class organization(models.Model):
    organization = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    phone = models.DecimalField(max_digits = 14, decimal_places = 0)
    signed_up = models.DateTimeField(auto_now_add = True)
    activated = models.BooleanField(default = False)

class events(models.Model):
    event = models.CharField(max_length = 200)
    location = models.CharField(max_length = 300)
    organization = models.ForeignKey(organization, on_delete = models.CASCADE, blank = True)
    after_days = models.DecimalField(max_digits = 4, decimal_places = 1)
    info = models.CharField(max_length = 500)
    activated = models.BooleanField(default = False)

class special_second(models.Model):
    special = models.ForeignKey(special, on_delete = models.CASCADE)
    age = models.DecimalField(max_digits = 3, decimal_places = 1)
    bio = models.CharField(max_length = 500)
    activities = models.CharField(max_length = 3, choices = activities_choices)
    disability = models.CharField(max_length  =3, choices = disability_choices)

class organization_second(models.Model):
    organization = models.ForeignKey(organization, on_delete = models.CASCADE)
    minimum_age = models.DecimalField(max_digits = 3, decimal_places = 1)
    maximum_age = models.DecimalField(max_digits = 3, decimal_places = 1)
    info = models.CharField(max_length = 500)
    activities = models.CharField(max_length = 3, choices = activities_choices)
    disability = models.CharField(max_length  =3, choices = disability_choices)

class activation_tbl(models.Model):
    organization = models.ForeignKey(organization, on_delete = models.CASCADE, blank = True, null = True)
    special = models.ForeignKey(special, on_delete = models.CASCADE, blank = True, null = True)
    session_key = models.CharField(max_length = 50)
    mobile_key = models.CharField(max_length = 5)
