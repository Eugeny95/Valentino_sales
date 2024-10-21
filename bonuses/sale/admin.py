from django.contrib import admin
from .models import UserIICO, UsersFilter, Position, SaleVolume, Sale, Promo





@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    @admin.action(description="Вернии  мне все апозиции")
    def get_position():
        print('GET POSITION!!!!!')

    

    list_display = ['name']
    actions = [get_position]
    

admin.site.register(UserIICO)
admin.site.register(UsersFilter)
admin.site.register(SaleVolume)
admin.site.register(Sale)
admin.site.register(Promo)
# Register your models here.


