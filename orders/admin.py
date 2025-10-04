from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at")   # total_price hatao abhi ke liye
    list_filter = ("status", "created_at")
    search_fields = ("id", "user__username")
    inlines = [OrderItemInline]   # Order ke andar OrderItems dikhenge

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")
    list_filter = ("order", "product")
    search_fields = ("product__name",)
