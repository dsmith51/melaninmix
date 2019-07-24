from django.contrib import admin

from .models import HomePage, About, Bio, Contact, Episode
# Register your models here.

admin.site.register(HomePage)
admin.site.register(About)
admin.site.register(Bio)
admin.site.register(Contact)
admin.site.register(Episode)
