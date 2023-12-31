from core.models import Product, Category, Seller, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist,Address


def default(request):
    categories = Category.objects.all()
    sellers = Seller.objects.all()
    try:
     address = Address.objects.get(user=request.user)
    except:
     address = None
    
    return {
        'categories':categories,
        'address':address,
        'sellers':sellers,
    }