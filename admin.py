from django.contrib import admin

# import your model
from collection.models  import Thing

# setup automatic slug creation
class Thingadmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug':('name',)}

# and register it
admin.site.register(Thing, ThingAdmin)