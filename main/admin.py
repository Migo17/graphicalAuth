from django.contrib import admin
from .models import PhotoCrypto, User
# Register your models here.
class PhotoCryptoAdmin(admin.ModelAdmin):
    fields = ['photo_name','photo_path']
admin.site.register(PhotoCrypto,PhotoCryptoAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'firstname', 'lastname', 'photo_password', 'generated_id']
admin.site.register(User, UserAdmin)
