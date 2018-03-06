from django.contrib import admin
from videos import models

class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title', 'length']
    list_filter = ['release_year', 'length']


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
