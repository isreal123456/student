from django.contrib import admin

from registration.models import result, course, student

# Register your models here.
admin.site.register(student)
admin.site.register(course)
admin.site.register(result)
