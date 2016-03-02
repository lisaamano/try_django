from django.contrib import admin
from .models import SignUp


class SignUpModelAdmin(admin.ModelAdmin):
    list_display = [
        '__unicode__',
        'timestamp',
        'updated',
    ]

    class Mate:
        model = SignUp

admin.site.register(SignUp, SignUpModelAdmin)
