from django.shortcuts import render, redirect
from MobileApp.models import CategoryDB
from MobileApp.models import ProductDB
from Frontend.models import contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index_page(req):
    return render(req, "index.html")


def category_page(request):
    data = CategoryDB.objects.all()
    return render(request, "AddCategory.html")


def category_save_data(request):
    if request.method == "POST":
        n = request.POST.get('name')
        d = request.POST.get('description')
        i = request.FILES['image']
        obj = CategoryDB(Name=n, Description=d, Image=i)
        obj.save()
        messages.success(request,"Category saved successfully ....!")
        return redirect(category_page)


def display_category(request):
    data = CategoryDB.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})


def edit_category(req, categoryid):
    data = CategoryDB.objects.get(id=categoryid)
    return render(req, "edit_page.html", {'data': data})


def update_category(req, categoryid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('description')
        try:
            pr = req.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(pr.name, pr)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=categoryid).Profile
        CategoryDB.objects.filter(id=categoryid).update(Name=na, Description=de, Image=file)
        return redirect(display_category)


def delete_category(req, categoryid):
    x = CategoryDB.objects.filter(id=categoryid)
    x.delete()
    return redirect(display_category)


def product_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "AddProducts.html", {'cat': cat})


def product_save_data(request):
    if request.method == "POST":
        ca = request.POST.get('category')
        na = request.POST.get('name')
        sp = request.POST.get('specification')
        ra = request.POST.get('rating')
        mr = request.POST.get('mrp_price')
        de = request.POST.get('deal_price')
        ds = request.POST.get('delivery_status')
        im = request.FILES['image']
        obj1 = ProductDB(Category=ca, Name=na, Specification=sp, Rating=ra, MRP_Price=mr, Deal_Price=de,
                         Delivery_Status=ds, Image=im)
        obj1.save()
        return redirect(product_page)


def display_product(request):
    data1 = ProductDB.objects.all()
    return render(request, "Product_Display.html", {'data1': data1})


def edit_product(req, productid):
    cat = CategoryDB.objects.all()
    data1 = ProductDB.objects.get(id=productid)
    return render(req, "edit_product.html", {'data1': data1, 'cat': cat})


def update_product(req, productid):
    if req.method == "POST":
        ca = req.POST.get('category')
        na = req.POST.get('name')
        sp = req.POST.get('specification')
        ra = req.POST.get('rating')
        mr = req.POST.get('mrp_price')
        de = req.POST.get('deal_price')
        ds = req.POST.get('delivery_status')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=productid).Image

        #
        # try:
        #     im2 = req.FILES['image2']
        #     fs2 = FileSystemStorage()
        #     file2 = fs2.save(im2.name, im2)
        # except MultiValueDictKeyError:
        #     file2 = ProductDB.objects.get(id=productid).Image2
        #
        # try:
        #     im3 = req.FILES['image3']
        #     fs3 = FileSystemStorage()
        #     file3 = fs3.save(im3.name, im3)
        # except MultiValueDictKeyError:
        #     file3 = ProductDB.objects.get(id=productid).Image3

        ProductDB.objects.filter(id=productid).update(Category=ca, Name=na, Specification=sp, Rating=ra, MRP_Price=mr,
                                                      Deal_Price=de, Delivery_Status=ds, Image=file)
        return redirect(display_product)


def delete_product(req, productid):
    x = ProductDB.objects.filter(id=productid)
    x.delete()
    return redirect(display_product)

def login_page(req):
    return render(req, "adminlogin.html")

def Admin_login(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('passwod')

        if User.objects.filter(username__contains =un).exists():
            x = authenticate(username=un, password=pwd)

            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index_page)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)



def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)



def contact_data(request):
    data = contactdb.objects.all()
    return render(request,"Contact_Data.html" ,{'data':data})


def delete_data(req, delid):
    x = contactdb.objects.filter(id=delid)
    x.delete()
    return redirect(contact_data)
