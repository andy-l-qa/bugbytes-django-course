from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Polls Admin"
admin.site.site_title = "The world's slickest Admin Panel"
admin.site.index_title = "Amazing Title"

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

