from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from MobileApp.models import CategoryDB
from MobileApp.models import ProductDB
from Frontend.models import contactdb,Registerdb,CartDB,checkoutdb
from django.contrib import messages



def Homepage(request):
    cat = CategoryDB.objects.all()
    data = CartDB.objects.filter(Username=request.session['name'])
    x = 0
    for d in data:
        x = x + d.Quantity
    return render(request,"Home.html", {'cat':cat , 'x':x})

def all_products(request):
    pro = ProductDB.objects.all()
    return render(request,"Allproducts.html",{'pro':pro})

# Create your views here.
def products_page(request,cat_name):
    data = ProductDB.objects.filter(Category=cat_name)
    return render(request,"Products.html",{'data':data})

def contact_us(request):
    return render(request,"Contactus.html")

def save_contact(re):
    if re.method=="POST":
        nam=re.POST.get('uname')
        mai=re.POST.get('mail')
        sub=re.POST.get('subj')
        mes=re.POST.get('mess')
        obje = contactdb(name=nam,email=mai,subject=sub,message=mes)
        obje.save()
    return redirect(contact_us)

def aboutus(request):
    return render(request,'aboutus.html')

def services(request):
    return render(request,'Services.html')

def singleproduct(request,proid):
    pro = ProductDB.objects.get(id=proid)
    return render(request,'Singleproduct.html',{'pro':pro})

def Register(request):
    return render(request,'Registration.html')

def login(request):
    return render(request,'login.html')

def save_register(re):
    if re.method=="POST":
        nam=re.POST.get('username')
        mai=re.POST.get('email')
        pas=re.POST.get('pass')
        cp=re.POST.get('cpass')
        im = re.FILES['image']
        obje = Registerdb(name=nam,email=mai,Password=pas,confirm_password=cp,Profile=im)
        obje.save()
    return redirect(Register)

def login_user(request):
    if request.method=="POST":
        un = request.POST.get("username")
        pwd = request.POST.get("pass")

        if Registerdb.objects.filter(name=un,Password=pwd).exists():
            request.session['name']=un
            request.session['Password']=pwd
            return redirect(Homepage)
        else:
            return redirect(login)
    return redirect(Homepage)


def logout_admin(request):
    del request.session['name']
    del request.session['Password']
    return redirect(login)

def save_cart(request):
    if request.method == "POST":
        use = request.POST.get('uname')
        pro = request.POST.get('pro_name')
        qua = request.POST.get('quantity')
        pri = request.POST.get('price')
        tot = request.POST.get('total_price')
        obj = CartDB(Username=use, Pro_Name=pro, Quantity=qua, Price=pri, Total_Price=tot)
        obj.save()
        return redirect(Homepage)
def cart_page(request):
    data=CartDB.objects.filter(Username=request.session['name'])
    x=0
    total=0
    for d in data:
        x=x+d.Quantity
        total=total+d.Total_Price
    return render(request,"cartpage.html",{'data':data , 'total':total , 'x':x})

def delete_cartpage(req, cartid):
    y = CartDB.objects.filter(id=cartid)
    y.delete()
    return redirect(cart_page)

def checkout_page(request):
    data = CartDB.objects.filter(Username=request.session['name'])
    total = 0
    for d in data:
        total = total + d.Total_Price
    return render(request,"checkout.html", {'data':data , 'total':total})

def save_checkout(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        em = request.POST.get('email')
        add = request.POST.get('address')
        cty = request.POST.get('city')
        cou = request.POST.get('country')
        pin = request.POST.get('pincode')
        num = request.POST.get('tel')
        obj = checkoutdb(name=nam, email=em, address=add, city=cty, country=cou,pincode=pin,number=num)
        obj.save()
        messages.success(request, "success")
        return redirect(Homepage)