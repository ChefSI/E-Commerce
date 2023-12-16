from django.urls import path
from core.views import product_list_view,category_list_view,product_category_list_view,seller_list_view,seller_detail_view,product_detail_view,tag_list, ajax_add_review,search_view,index

app_name= "core"

urlpatterns = [

    #HomePage
    path('',index,name='index'),

    #Products
    path("products/",product_list_view,name="product-list"),
    path("products/<pid>",product_detail_view,name="product-detail"),

    #Categories
    path("category/",category_list_view,name="category-list"),
    path("category/<cid>/",product_category_list_view,name="product-category-list"),
    
    #Seller
    path("seller/",seller_list_view,name="seller-list"),
    path("seller/<sid>/",seller_detail_view,name="seller-detail"),

    #Tags
    path("products/tag/<slug:tag_slug>/",tag_list,name="tag"),

    #Reviews
    path("ajax-add-review/<pid>/", ajax_add_review, name="ajax-add-review"),

    #Search
    path("search/",search_view, name="search")

]                                                                                                                                                                                                                                                                                                                                                                                                                                                                     