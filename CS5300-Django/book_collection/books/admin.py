from django.contrib import admin

from .models import Author
from .models import Binding
from .models import Book
from .models import Copy
from .models import Grade
from .models import Language
from .models import Publisher
from .models import WrittenBy

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class BindingAdmin(admin.ModelAdmin):
    list_display = ['binding_type']

class BookAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'publisher', 'publication_date']

class CopyAdmin(admin.ModelAdmin):
    list_display = ['book', 'edition', 'price', 'binding', 'grade', 'has_jacket']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['label']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language_code']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher_name']

class WrittenByAdmin(admin.ModelAdmin):
    list_display = ['book', 'author']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Binding, BindingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Copy, CopyAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(WrittenBy, WrittenByAdmin)