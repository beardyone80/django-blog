from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """Allows rich-text editing of content in admin
    """
    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)
