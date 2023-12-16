from django.contrib import admin
from core.models import Product, Category, Seller, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist,Address
   
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user' , 'title' , 'product_image' , 'price' , 'category' , 'seller' , 'featured' , 'product_status' , 'pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'category_image' ,]


class SellerAdmin(admin.ModelAdmin):
    list_display = ['title' , 'seller_image' ,]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user' , 'price' ,'paid_status' , 'order_date' , 'product_status']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order' , 'invoice_no', 'item' , 'image','quantity' , 'price' , 'total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'review' , 'rating']


class WishListAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user' , 'address' , 'status'  ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, WishListAdmin)
admin.site.register(Address, AddressAdmin)

