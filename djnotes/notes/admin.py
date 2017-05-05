from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
 	list_display = (
 		'id',
 		'title',
 		'note',
 	)
 	search_fields = (
 		'title',
 		'note',
 	)


admin.site.register(Note, NoteAdmin)
