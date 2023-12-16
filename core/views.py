from math import prod
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Count,Avg
from taggit.models import Tag

from core.models import Product, Category, Seller, CartOrder, CartOrderItems, ProductImages, ProductReview, wishlist,Address
from core.forms import ProductReviewForm
 
# Create your views here.

def index(request):
    products = Product.objects.filter(product_status="published",featured=True)

    context = {
        "products":products
    }
    return render(request,'core/index.html',context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {
        "products":products
    }
    return render(request,'core/product-list.html',context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }
    return render(request,'core/category-list.html',context)


def product_category_list_view(request,cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category":category,
        "products":products,
    }
    return render(request,'core/product-category-list.html',context)

def seller_list_view(request):
    sellers = Seller.objects.all()
    context = {
        "sellers":sellers,
    }
    return render(request, "core/seller-list.html",context)

def seller_detail_view(request,sid):
    seller = Seller.objects.get(sid=sid)
    products = Product.objects.filter(seller=seller,product_status="published")
    context = {
        "seller":seller,
        "products":products,
    }
    return render(request, "core/seller-detail.html",context)

def product_detail_view(request,pid):
    product = Product.objects.get(pid=pid)
    product_images = product.product_images.all()
    product_cat = Product.objects.filter(category=product.category).exclude(pid=pid)
    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    avg_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    review_form = ProductReviewForm()
    make_review= True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False
    context = {
        "product":product,
        "product_images":product_images,
        "product_cat":product_cat,
        "reviews":reviews,
        "avg_rating":avg_rating,
        "review_form":review_form,
        "make_review":make_review,
    }
    return render(request, "core/product-detail.html",context)

def tag_list(request,tag_slug=None):
    products=Product.objects.filter(product_status="published").order_by("-id")

    tag=None
    if tag_slug:
      tag=get_object_or_404(Tag, slug=tag_slug)
      products = products.filter(tags__in=[tag])
    
    context ={
        "products": products,
        "tag": tag
    } 
    return render(request, "core/tag.html", context)

def ajax_add_review(request,pid):
    product = Product.objects.get(pid=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    avg_reviews= ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse(
        {
        'bool': True,
        'context': context,
        'avg_reviews': avg_reviews,
        }
    )

def search_view(request):
    query = request.GET.get("q")

    products = Product.objects.filter(title__icontains=query).order_by("-date")
 
    context = {
        "products": products,
        "query": query,
        
    }
    return render(request, "core/search.html", context)