from django.urls import path
from MobileApp import views

urlpatterns = [
    path('index_page/', views.index_page, name="index_page"),
    path('category_page/', views.category_page, name="category_page"),
    path('category_save_data/', views.category_save_data, name="category_save_data"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:categoryid>/', views.edit_category, name="edit_category"),
    path('update_category/<int:categoryid>/', views.update_category, name="update_category"),
    path('delete_category/<int:categoryid>/', views.delete_category, name="delete_category"),


    path('product_page/', views.product_page, name="product_page"),
    path('product_save_data/', views.product_save_data, name="product_save_data"),
    path('display_product/', views.display_product, name="display_product"),
    path('update_product/<int:productid>/', views.update_product, name="update_product"),
    path('delete_product/<int:productid>/', views.delete_product, name="delete_product"),
    path('edit_product/<int:productid>/', views.edit_product, name="edit_product"),

    path('login/', views.login_page, name="login"),
    path('Admin_login/', views.Admin_login, name="Admin_login"),
    path('Admin_logout/', views.Admin_logout, name="Admin_logout"),
    path('contact_data/', views.contact_data, name="contact_data"),
    path('delete_data/<int:delid>/', views.delete_data, name="delete_data"),

]