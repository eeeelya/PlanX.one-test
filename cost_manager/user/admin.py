from django.contrib import admin

from user.models import User, UserTransactions, UserCategories

admin.site.register(User)
admin.site.register(UserTransactions)
admin.site.register(UserCategories)
