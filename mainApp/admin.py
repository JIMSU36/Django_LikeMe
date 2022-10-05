from django.contrib import admin
from .models import Instructor, Trainer, Gallery
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Trainer)
admin.site.register(Gallery)