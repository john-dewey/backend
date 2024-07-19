from django.contrib import admin
from .models import Messages, Account, Token

#Admin Page For Messages API
class MessagesAdmin(admin.ModelAdmin):
    #This list will display all of the Messages in our DB
    list_display = ('name', 'email', 'message')


class AccountAdmin(admin.ModelAdmin):
    #This list will display all of the Messages in our DB
    list_display = ('username', 'password', 'email')




# Register your models here.

admin.site.register(Messages, MessagesAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Token)