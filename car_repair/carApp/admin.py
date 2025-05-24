from django.contrib import admin
from .models import Car, Repair, Manufacturer, WorkShop, WorkShopManufacturer,FixRequest

# Register your models here.

class WorkShopManufacturerInline(admin.StackedInline):
    model = WorkShopManufacturer
    extra = 1


class WorkShopAdmin(admin.ModelAdmin):
    inlines = [WorkShopManufacturerInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class RepairAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.user = request.user

        super(RepairAdmin, self).save_model(request, obj, form, change)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True


class CarAdmin(admin.ModelAdmin):
    list_display = ('maxSpeed', 'type')


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(WorkShop, WorkShopAdmin)
admin.site.register(WorkShopManufacturer)
admin.site.register(FixRequest)