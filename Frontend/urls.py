from django.urls import path
from Frontend import views

urlpatterns=[
    path('Homepage/',views.Homepage,name="Homepage"),
    path('all_products/',views.all_products,name="all_products"),
    path('products_page/<cat_name>/',views.products_page,name="products_page"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('services/', views.services, name="services"),
    path('singleproduct/<int:proid>/', views.singleproduct, name="singleproduct"),
    path('Register/', views.Register, name="Register"),
    path('login/', views.login, name="login"),
    path('logout_admin/', views.logout_admin, name="logout_admin"),
    path('save_register/', views.save_register, name="save_register"),
    path('login_user/', views.login_user, name="login_user"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('delete_cartpage/<int:cartid>/', views.delete_cartpage, name="delete_cartpage"),

]